@echo off
set /p InstallPython=Would you like to install Python [y/n]?
if %InstallPython%==y ("./Installer1.bat") else (echo "Unknown value") 
if %InstallPython%==n ("./Installer2.bat") else (echo "Unknown value")