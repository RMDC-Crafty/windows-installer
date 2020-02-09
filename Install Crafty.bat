@echo off
set /p InstallPython=Would you like to install Python [y/n]?
if %InstallPython%==y ("./Install Crafty(With Python).bat") else (echo "Unknown value") 
if %InstallPython%==n ("./Install Crafty(Without Python).bat") else (echo "Unknown value")