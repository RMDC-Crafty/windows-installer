set /P CraftyPath=Please Enter The Path Crafty Is Installed To (This Is The Same Path You Entered Into The Installer):
set /P Python=Please Enter The Location Of Your Python Installation(Give The Path To python.exe Including python.exe On The End e.g: C:\Program Files\Python37\python.exe)
path %path%;%CD%\NSSM\win64\
nssm install CraftyController %Python% %CraftyPath%\crafty.py -d
nssm set CraftyController AppDirectory %CraftyPath%
nssm start CraftyController