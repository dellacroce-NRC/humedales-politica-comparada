@echo off
title Humedales urbanos - Streamlit
cd /d "%~dp0"

echo.
echo Iniciando la aplicacion de Humedales Urbanos...
echo.
echo Si es la primera vez y falta alguna libreria, ejecuta:
echo python -m pip install -r requirements.txt
echo.

python -m streamlit run app.py

echo.
echo La aplicacion se detuvo. Puedes cerrar esta ventana.
pause

