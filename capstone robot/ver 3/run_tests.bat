@echo off
setlocal

cd /d "%~dp0"

:: ── Stable Timestamp ───────────────────────────────────
for /f %%i in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd_HH-mm-ss"') do set TS=%%i

set FINAL_REPORT=report_%TS%.html

echo.
echo  ====================================================
echo   Running TC002_Login
echo  ====================================================
echo.

if not exist results mkdir results

:: ── Run Robot Normally (default names) ─────────────────
robot --outputdir results tests\TC002_Login.robot

:: ── Rename ONLY AFTER execution completes ──────────────
rename "results\report.html" "%FINAL_REPORT%"

echo.
echo  ====================================================
echo   DONE — Report renamed to:
echo   results\%FINAL_REPORT%
echo  ====================================================
echo.

start "" "results\%FINAL_REPORT%"

endlocal
pause