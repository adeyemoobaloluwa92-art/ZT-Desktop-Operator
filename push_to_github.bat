@echo off
title Push ZT-Desktop-Operator to GitHub
echo ========================================================
echo Pushing to: https://github.com/adeyemoobaloluwa92-art/ZT-Desktop-Operator
echo ========================================================
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" push_to_github.py %*
pause
