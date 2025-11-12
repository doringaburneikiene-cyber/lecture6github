import streamlit as st
import ollama
from PIL import Image
import io
import base64

def encode_image_to_base64(image_file):
    """Convert uploaded image to base64 string for Ollama"""
    if image_file is not None:
        # Convert to PIL Image
        image = Image.open(image_file)
        
        # Convert to bytes
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        image_bytes = buffer.getvalue()
        
        # Encode to base64
        return base64.b64encode(image_bytes).decode()
    return None

def analyze_image(image_base64):
    """Analyze image using Ollama llava:7b model"""
    try:
        response = ollama.chat(
            model='llava:7b',
            messages=[{
                'role': 'user',
                'content': 'Apibūdink šio paveikslėlio turinį lietuvių kalba. Būk tikslus ir detalus. Aprašyk ką matai, kokios spalvos, objektai, žmonės, veiksmai.',
                'images': [image_base64]
            }]
        )
        return response.message.content
    except Exception as e:
        return f"Klaida analizuojant paveikslėlį: {str(e)}"

def main():
    st.set_page_config(
        page_title="Paveikslėlių analizė su AI",
        page_icon="🖼️",
        layout="wide"
    )
    
    st.title("🖼️ Paveikslėlių analizė su dirbtinio intelekto pagalba")
    st.markdown("---")
    
    # Informacija apie programą
    with st.expander("ℹ️ Informacija apie programą"):
        st.markdown("""
        **Ši programa naudoja:**
        - **Streamlit** - interaktyviai sąsajai
        - **Ollama** su **LLaVA 7b** modeliu - paveikslėlių analizei
        - **Python PIL** - paveikslėlių apdorojimui
        
        **Kaip naudoti:**
        1. Įkelkite paveikslėlį naudodami failų įkėlimo funkciją
        2. Palaukite, kol dirbtinis intelektas išanalizuos turinį
        3. Peržiūrėkite detalų aprašymą
        """)
    
    # Pagrindinis turinys
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.header("📤 Įkelkite paveikslėlį")
        
        uploaded_file = st.file_uploader(
            "Pasirinkite paveikslėlį analizei",
            type=['png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'],
            help="Palaikomi formatai: PNG, JPG, JPEG, GIF, BMP, WEBP"
        )
        
        if uploaded_file is not None:
            # Rodyti įkeltą paveikslėlį
            image = Image.open(uploaded_file)
            st.image(
                image, 
                caption=f"Įkeltas failas: {uploaded_file.name}",
                use_container_width=True
            )
            
            # Failo informacija
            st.info(f"""
            **Failo informacija:**
            - Pavadinimas: {uploaded_file.name}
            - Dydis: {uploaded_file.size:,} baitų
            - Formatas: {image.format}
            - Matmenys: {image.size[0]} x {image.size[1]} pikselių
            """)
    
    with col2:
        st.header("🤖 AI analizės rezultatai")
        
        if uploaded_file is not None:
            if st.button("🔍 Analizuoti paveikslėlį", type="primary", use_container_width=True):
                with st.spinner("Dirbtinis intelektas analizuoja paveikslėlį... ⏳"):
                    # Konvertuoti paveikslėlį į base64
                    image_base64 = encode_image_to_base64(uploaded_file)
                    
                    if image_base64:
                        # Gauti analizės rezultatus
                        analysis_result = analyze_image(image_base64)
                        
                        # Rodyti rezultatus
                        st.success("✅ Analizė baigta!")
                        
                        with st.container(border=True):
                            st.markdown("### 📝 Paveikslėlio aprašymas:")
                            st.markdown(analysis_result)
                        
                        # Galimybė atsisiųsti rezultatus
                        st.download_button(
                            label="📄 Atsisiųsti aprašymą",
                            data=analysis_result,
                            file_name=f"analizes_rezultatas_{uploaded_file.name}.txt",
                            mime="text/plain",
                            help="Atsisiųskite analizės rezultatus kaip tekstinį failą"
                        )
                    else:
                        st.error("Nepavyko apdoroti paveikslėlio.")
        else:
            st.info("👆 Pirmiausia įkelkite paveikslėlį kairiajame stulpelyje")
    
    # Papildoma informacija apačioje
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 0.8em;'>
        Sukurta naudojant Streamlit ir Ollama LLaVA modelį | 
        Paveikslėlių analizė su dirbtinio intelekto pagalba
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()