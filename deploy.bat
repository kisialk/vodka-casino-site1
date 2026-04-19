@echo off
setlocal EnableExtensions
cd /d "%~dp0"

REM ============================================================
REM  Токен и пароль GitHub СЮДА НЕ КЛАДИТЕ — файл может утечь.
REM  При push Windows спросит логин/пароль ОДИН РАЗ и сохранит
REM  в Git Credential Manager (не в этом файле).
REM  Пароль в поле пароля = НОВЫЙ Personal Access Token (не от чата).
REM  Замените YOUR_REPO на имя репозитория на github.com/kisialk/...
REM ============================================================

echo === GIT USER (для подписи коммита, не секрет) ===
git config user.name "kisialk"
git config user.email "kisialk@users.noreply.github.com"

echo === GIT INIT (если ещё нет .git) ===
if not exist ".git" git init

echo === REMOTE origin ===
git remote get-url origin >nul 2>&1
if errorlevel 1 (
  git remote add origin "https://github.com/kisialk/YOUR_REPO.git"
  echo Добавлен remote. Если ошибка — отредактируйте YOUR_REPO в deploy.bat
) else (
  echo Remote уже есть:
  git remote -v
)

echo === ADD ===
git add .

echo === COMMIT ===
git commit -m "Initial commit: SEO pages + affiliate"
if errorlevel 1 (
  echo Коммит не создан: нет изменений или уже закоммичено. Продолжаю push...
)

echo === ВЕТКА main ===
git branch -M main

echo === PUSH в GitHub ===
echo.
echo  Сейчас откроется запрос учётных данных или браузер.
echo  Username: kisialk
echo  Password: вставьте НОВЫЙ GitHub PAT (Settings - Developer settings - Tokens^)
echo.
git push -u origin main
if errorlevel 1 (
  echo.
  echo PUSH не удался. Проверьте: 1^) YOUR_REPO в remote  2^) токен не отозван  3^) git установлен
)

echo === DONE ===
pause
endlocal
