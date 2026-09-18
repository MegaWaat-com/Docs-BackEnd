@echo off
chcp 65001 >nul

:: --- تنظیم معماری تفکیک‌شده گیت و گوگل‌درایو ---
set "GIT_DIR=C:\GitMeta\Docs-BackEnd\.git"
set "GIT_WORK_TREE=G:\My Drive\Docs-BackEnd"

:: رفتن به پوشه اصلی کاری در گوگل‌درایو
cd /d "%GIT_WORK_TREE%"

echo ======================================================
echo MEGAWAAT DOCUMENTATION - Syncing...
echo ======================================================

echo [1/3] Processing Word, Excel and Images...
:: اگر فایل پایتون در پوشه _scripts است مسیرش را _scripts\sync_specs.py بگذار، در غیر این صورت همین خط زیر:
python sync_specs.py
if %errorlevel% neq 0 goto :error

echo [2/3] Checking Git Status...
git add .
git status

echo [3/3] Committing and Pushing...
set /p commit_msg="Enter commit message: "
if "%commit_cp 65001 >nul`)** است؛ یعنی قبل از اینکه هرگونه دستور `git` اجرا شود، متغیرهای محیطی ست شوند تا تمام دستورات بعدی گیت بدانند مغز دیتابیس کجاست و فایل‌ها کجا قرار دارند.

فقط یک نکته کلیدی: وقتی مسیرها فاصله (Space) دارند (مثل `My Drive`)، متغیرها را داخل کوتیشن جفت نگذارید، بلکه نام متغیر و مقدار را داخل پرانتز یا مستقیماً بدون فاصله اضافی بنویسید. همچنین برای اینکه دستور پایتون هم دقیقاً بداند کجا اجرا شود، یک خط تغییر مسیر (`cd /d`) هم نیاز دارد.

فایل `sync.bat` اصلاح‌شده و نهایی شما به این صورت می‌شود:
```bat
@echo off
chcp 65001 >nul

:: --- تنظیم معماری تفکیک‌شده گیت و گوگل‌درایو ---
set "GIT_DIR=C:\GitMeta\Docs-BackEnd\.git"
set "GIT_WORK_TREE=G:\My Drive\Docs-BackEnd"

:: رفتن به پوشه اصلی کاری در گوگل‌درایو
cd /d "%GIT_WORK_TREE%"

echo ======================================================
echo MEGAWAAT DOCUMENTATION - Syncing...
echo ======================================================

echo [1/3] Processing Word, Excel and Images...
:: اگر فایل پایتون در پوشه _scripts است مسیرش را _scripts\sync_specs.py بگذار، در غیر این صورت همین خط زیر:
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

echo.
echo تمام عملیات با موفقیت انجام شد!
pause
exit

:error
echo.
echo [!] یک خطا در عملیات رخ داد. لطفاً پیام خطای بالا