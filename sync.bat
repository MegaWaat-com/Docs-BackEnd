@echo off
chcp 65001 >nul
echo ======================================================
echo MEGAWAAT DOCUMENTATION - Syncing...
echo ======================================================

echo [1/3] Processing Word, Excel and Images...
python sync_specs.py
if %errorlevel% neq 0 goto :error

echo [2/3] Checking Git Status...
git add .
git status

echo [3/3] Committing and Pushing...
set /p commit_msg="Enter commit message: "
if "%commit_msg%"=="" set commit_msg=Update docs via automation
git commit -m "%commit_msg%"
git push origin main

if %errorlevel% neq 0 goto :error

echo تمام عملیات با موفقیت انجام شد!
pause
exit

:error
echo.
echo [!] یک خطا در عملیات رخ داد. لطفاً پیام خطای بالا را بررسی کنید.
pause
