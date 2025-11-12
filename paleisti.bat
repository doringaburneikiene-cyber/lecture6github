@echo off
echo ===============================================
echo     Paveiksleliu analizes programos paleidimas
echo ===============================================
echo.

REM Patikrinti ar yra virtuali aplinka
if not exist ".venv" (
    echo Sukuriama virtuali aplinka...
    python -m venv .venv
    echo.
)

REM Aktyvinti virtualia aplinka
echo Aktyvinama virtuali aplinka...
call .venv\Scripts\activate.bat

REM Diegti priklausomybes jei reikia
echo Tikrinam ir diegiam priklausomybes...
.venv\Scripts\pip.exe install streamlit ollama Pillow --quiet
echo.

REM Patikrinti ar veikia Ollama
echo Tikrinam Ollama konfiguracija...
.venv\Scripts\python.exe -c "import ollama; ollama.list()" >nul 2>&1

if %ERRORLEVEL% equ 0 (
    echo ✓ Ollama aptikta! Paleidziama pilna versija...
    echo.
    echo ===============================================
    echo  Programos URL: http://localhost:8501
    echo ===============================================
    echo.
    .venv\Scripts\python.exe -m streamlit run app.py
) else (
    echo ! Ollama neaptikta. Paleidziama DEMO versija...
    echo.
    echo ===============================================
    echo  DEMO programos URL: http://localhost:8501
    echo  
  echo  Pilnai versijai reikia:
  echo  1. Idiegti Ollama: https://ollama.ai  
  echo  2. Paleisti: ollama serve
  echo  3. Atsisiusti modeli: ollama pull llava:7b
    echo ===============================================
    echo.
    .venv\Scripts\python.exe -m streamlit run demo_app.py
)

pause