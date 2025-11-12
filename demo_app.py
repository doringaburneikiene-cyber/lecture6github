import streamlit as st
import base64
import io
from PIL import Image

def encode_image_to_base64(image_file):
    """Convert uploaded image to base64 string"""
    if image_file is not None:
        image = Image.open(image_file)
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG")
        image_bytes = buffer.getvalue()
        return base64.b64encode(image_bytes).decode()
    return None

def analyze_image_demo(image_base64):
    """Demo function when Ollama is not available"""
    return """
    **DEMO REŽIMAS** (Ollama nepavyko prisijungti)
    
    Ši programa demonstruja paveikslėlių analizės sąsają. 
    Tikroje versijoje dirbtinis intelektas išanalizuotų paveikslėlio turinį ir pateiktų detalų aprašymą.
    
    **Kad programa veiktų pilnai:**
    1. Įdiekite Ollama (https://ollama.ai)
    2. Paleiskite: `ollama serve`
    3. Atsisiųskite modelį: `ollama pull gemma2:2b`
    4. Paleiskite programą iš naujo
    
    **Paveikslėlio informacija:**
    - Formato analizė: ✅ Veikia
    - Dydžio analizė: ✅ Veikia  
    - AI turinio analizė: ⏳ Laukia Ollama konfigūracijos
    """

def main():
    st.set_page_config(
        page_title="Paveikslėlių analizė su AI - DEMO",
        page_icon="🖼️",
        layout="wide"
    )
    
    st.title("🖼️ Paveikslėlių analizės DEMO versija")
    st.warning("⚠️ Ši yra demo versija. Pilnai funkcionali versija reikalauja Ollama konfigūracijos.")
    st.markdown("---")
    
    # Informacija apie demo
    with st.expander("ℹ️ Demo versijos informacija"):
        st.markdown("""
        **Demo versija demonstruoja:**
        - Streamlit sąsają
        - Paveikslėlių įkėlimą ir apdorojimą
        - Failų formato analizę
        
        **Pilnai versijai reikia:**
        - Ollama tarnybos (ollama serve)
        - Gemma2:2b modelio (ollama pull gemma2:2b)
        - Internetinio ryšio pirmam modelio atsisiuntimui
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
            image = Image.open(uploaded_file)
            st.image(
                image, 
                caption=f"Įkeltas failas: {uploaded_file.name}",
                use_container_width=True
            )
            
            st.info(f"""
            **Failo informacija:**
            - Pavadinimas: {uploaded_file.name}
            - Dydis: {uploaded_file.size:,} baitų
            - Formatas: {image.format}
            - Matmenys: {image.size[0]} x {image.size[1]} pikselių
            """)
    
    with col2:
        st.header("🤖 Demo analizės rezultatai")
        
        if uploaded_file is not None:
            if st.button("🔍 Rodyti demo analizę", type="primary", use_container_width=True):
                with st.spinner("Ruošiama demo analizė... ⏳"):
                    image_base64 = encode_image_to_base64(uploaded_file)
                    
                    if image_base64:
                        demo_result = analyze_image_demo(image_base64)
                        
                        st.warning("🧪 Demo rezultatai")
                        
                        with st.container(border=True):
                            st.markdown("### 📝 Demo aprašymas:")
                            st.markdown(demo_result)
                        
                        st.download_button(
                            label="📄 Atsisiųsti demo aprašymą",
                            data=demo_result,
                            file_name=f"demo_analizes_rezultatas_{uploaded_file.name}.txt",
                            mime="text/plain"
                        )
                    else:
                        st.error("Nepavyko apdoroti paveikslėlio.")
        else:
            st.info("👆 Pirmiausia įkelkite paveikslėlį kairiajame stulpelyje")
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray; font-size: 0.8em;'>
        Demo versija | Pilnai funkcionali versija reikalauja Ollama konfigūracijos
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()