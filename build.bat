@echo off
pyinstaller -w --runtime-hook pyinstaller.hook.py --add-data "src\assets;assets" --icon favicon.ico --name ai_ui src\ai_client.py -y

set BackupPath=%~dp0
cd dist\ai_ui 
ai_ui.exe
cd %BackupPath%