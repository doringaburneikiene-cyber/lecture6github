# Paveikslėlių analizės programa su AI

Ši programa naudoja Streamlit sąsają ir Ollama LLaVA 7B modelį paveikslėlių turinio analizei ir aprašymui.

## Funkcionalumas

- **Interaktyvi web sąsaja** su Streamlit
- **Paveikslėlių įkėlimas** (PNG, JPG, JPEG, GIF, BMP, WEBP formatai)
- **AI analizė** naudojant Ollama LLaVA 7B modelį
- **Detalūs aprašymai** lietuvių kalba
- **Rezultatų eksportavimas** į tekstinius failus

## Reikalavimai

- Python 3.8+
- Ollama su LLaVA 7B modeliu
- Interneto ryšys (pirmam Ollama modelio atsisiuntimui)

## Diegimas

1. **Klonuokite projektą:**
```bash
git clone <repo-url>
cd lecture6github
```

2. **Sukurkite virtualią aplinką:**
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

3. **Įdiekite priklausomybes:**
```bash
pip install -r requirements.txt
```

4. **Įdiekite ir paleiskite Ollama:**
- Atsisiųskite Ollama iš https://ollama.ai
- Įdiekite programą
- Paleiskite terminalą ir vykdykite:
```bash
ollama serve
```
- Naujame terminale atsisiųskite modelį:
```bash
ollama pull llava:7b
```

## Paleidimas

1. **Įsitikinkite, kad Ollama veikia:**
```bash
ollama serve
```

2. **Paleiskite Streamlit programą:**
```bash
streamlit run app.py
```

3. **Atidarykite naršyklę** ir eikite į http://localhost:8501

## Naudojimas

1. Įkelkite paveikslėlį naudodami failų įkėlimo funkciją
2. Spauskite "Analizuoti paveikslėlį" mygtuką
3. Palaukite, kol AI išanalizuos turinį
4. Peržiūrėkite detalų aprašymą
5. Atsisiųskite rezultatus, jei reikia

## Techninė informacija

- **Frontend:** Streamlit
- **AI modelis:** Ollama LLaVA 7B
- **Paveikslėlių apdorojimas:** Python PIL (Pillow)
- **Kodavimas:** Base64 paveikslėlių perdavimui

## Troubleshooting

### Ollama neveikia
- Įsitikinkite, kad Ollama tarnybą paleista: `ollama serve`
- Patikrinkite, ar modelis atsisiųstas: `ollama list`

### Modelio klaidos
- Atsisiųskite modelį: `ollama pull llava:7b`
- Patikrinkite modelio pavadinimą programos kode

### Streamlit klaidos
- Įsitikinkite, kad visos priklausomybės įdiegtos: `pip install -r requirements.txt`
- Patikrinkite Python versiją: `python --version`

## Kūrėjai

Sukurta pagal instrukcijas naudojant:
- Streamlit dokumentaciją
- Ollama Python bibliotekos dokumentaciją
- AI modelio integracijos geriausias praktikas
