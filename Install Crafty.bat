@echo off
set /p InstallPython=Would you like to install Python [y/n]?
if %InstallPython%==y ("Python Installer.exe" PrependPath=1 InstallAllUsers=1 AssociateFiles=1 Include_lib=1 Include_pip=1 Include_tcltk=1 Include_tools=1 SimpleInstall=1 SimpleInstallDescription="Click Me!" && "%localappdata%\Programs\Python\Python37\python.exe" Installer.py ) else (python Installer.py)
set /p UpdateFile=Would you like to add a crafty update file [y/n]?
if %UpdateFile%==y (Git.bat) else (echo Not Creating Update File)