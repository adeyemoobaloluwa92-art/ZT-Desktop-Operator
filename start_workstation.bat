@echo off
title Zero-Token Desktop Operator AI (Gemma 4)
echo ===================================================
echo Starting Zero-Token Desktop Operator AI Server...
echo UI will open at http://localhost:8000
echo ===================================================
start http://localhost:8000
python agent_server.py
if %ERRORLEVEL% NEQ 0 (
    "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" agent_server.py
)
pause
