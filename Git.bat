@echo off
set /p CraftyPath=Please Confirm The Path You Selected For Crafty To Install To:
powershell Expand-Archive Git.zip -DestinationPath "%CraftyPath%\GitPortable"
copy "Update File Creator.py" "%CraftyPath%\Update File Creator.py"
cd %CraftyPath%
python "Update File Creator.py"
del "Update File Creator.py"
pause