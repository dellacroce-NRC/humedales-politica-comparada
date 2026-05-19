@echo off
title Instalar librerias - Humedales urbanos
cd /d "%~dp0"

echo.
echo Instalando librerias necesarias...
echo.

python -m pip install -r requirements.txt

echo.
echo Instalacion terminada. Ahora puedes abrir INICIAR_APP.bat
pause

