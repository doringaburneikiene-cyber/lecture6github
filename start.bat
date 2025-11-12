@echo off
echo Paleidziama paveiksleliu analizes programa...
echo.

REM Patikrinti ar yra virtuali aplinka
if not exist ".venv" (
    echo Sukuriama virtuali aplinka...
    python -m venv .venv
)

REM Aktyvinti virtualia aplinka
echo Aktyvinama virtuali aplinka...
call .venv\Scripts\activate.bat

REM Diegti priklausomybes
echo Diegiamos priklausomybes...
pip install -r requirements.txt

echo.
echo ===============================================
echo  SVARBU: Prasome isitikinti, kad:
echo  1. Ollama yra idiegta ir paleista (ollama serve)
echo  2. Gemma2:2b modelis yra atsisiustas (ollama pull gemma2:2b)
echo ===============================================
echo.

REM Paleisti Streamlit aplikacija
echo Paleidziama Streamlit aplikacija...
streamlit run app.py

pause