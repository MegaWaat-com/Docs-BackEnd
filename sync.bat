@echo off
chcp 65001 > nul
echo ======================================================
echo    MEGAWAAT DOCUMENTATION & ARCHITECTURE ENGINE
echo ======================================================
echo.

echo [1/3] Processing Word, Excel and Images...
python sync_specs.py
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python script failed! Check python/pandoc installation.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [2/3] Checking Git Status...
git status --porcelain > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Git repository not initialized yet or not found.
    echo Converted files are ready locally.
    pause
    exit /b 0
)

echo.
echo [3/3] Committing & Pushing to GitHub...
git add .
set /p commit_msg="Enter commit message (Press Enter for auto date): "
if "%commit_msg%"=="" set commit_msg=Update docs and architecture: %date% %time%

git commit -m "%commit_msg%"
git push

echo.
echo ======================================================
echo    ALL DONE! EVERYTHING IS IN SYNC WITH GITHUB.
echo ======================================================
pause
