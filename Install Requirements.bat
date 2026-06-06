@echo off
cd /d "%~dp0"

where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    py -3 -m venv .venv
    if not exist ".venv\Scripts\python.exe" (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
    ".venv\Scripts\python.exe" -m pip install --upgrade pip
    ".venv\Scripts\python.exe" -m pip install -r requirements.txt
) else (
    python -m venv .venv
    if not exist ".venv\Scripts\python.exe" (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
    ".venv\Scripts\python.exe" -m pip install --upgrade pip
    ".venv\Scripts\python.exe" -m pip install -r requirements.txt
)

echo.
echo Dependencies installed successfully.
echo You can now double-click Launch Invoice Generator.bat
pause
