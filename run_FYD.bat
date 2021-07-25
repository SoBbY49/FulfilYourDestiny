@echo off
python --version
if %ERRORLEVEL% EQU 0 ( 
  REM python is installed, run our game
   python FYD.py
) ELSE (
 REM Install python
 python
)