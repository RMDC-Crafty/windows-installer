@echo off
path %path%;%CD%\NSSM\win64\
nssm remove CraftyController
echo Removed!