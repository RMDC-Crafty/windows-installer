import os
import sys
import subprocess
import time

def clone():
    global path
    global branch
    global remote_url
    """Clone a repo in a give path and update the working directory with
    a checkout to head (GIT_CHECKOUT_SAFE_CREATE)

    :param str remote_url: URL of the repository to clone

    :param str path: Local path to clone into

    :param str branch: Branch to checkout after the
    clone. The default is to use the remote's default branch.

    """
    from pathlib import Path
    path = path + "\Crafty"
    data_folder = Path(path)
    repo = pygit2.clone_repository(remote_url, path, checkout_branch=branch)
    repo.checkout_head()
    file_to_open = data_folder / "run_crafty.bat"
    reqfile_to_open = data_folder / "requirements.txt"
    file = open(file_to_open, "w")
    file.write("python crafty.py")
    file.close()
    file_to_open = data_folder / "run_crafty_verbose.bat"
    file = open(file_to_open, "w")
    file.write("python crafty.py -v")
    file.close()
    file = open(reqfile_to_open, "r")

    for line in file:
        req = line.split("/n")
        command_list = [sys.executable, "-m", "pip", "install", "--user", req]
        with subprocess.Popen(command_list, stdout=subprocess.PIPE) as proc:
            print(proc.stdout.read())
    if service == 'yes':
        sg.popup("Please Run Install Service.bat In The Same Directory As This File With Administrative Privilages! (Right Click, Run As Administrator)")
    else:
        sg.popup("Crafty Install Complete!")
def GUI():
    global remote_url
    global path
    global branch
    global service
    sg.theme("DefaultNoMoreNagging")
    layout = [[sg.Text('Please Enter The Path You Would Like Crafty To Install To:')],
                [sg.InputText()],
                [sg.Submit()]]

    window = sg.Window('Enter A Path', layout)
    window.Finalize()
    window.TKroot.focus_force()
    event, values = window.read()
    window.close()

    text_input = values[0]
    path = text_input

    layout = [[sg.Text('Please Enter The Branch You Would Like To Clone: (You Can Choose From "Master", "Dev", "Snapshot" And "Beta")')],
              [sg.InputText()],
              [sg.Submit()]]

    window = sg.Window('Enter A Branch', layout)
    window.Finalize()
    window.TKroot.focus_force()
    event, values = window.read()
    window.close()

    text_input = values[0]
    branch = text_input
    branch = branch.lower()

    layout = [[sg.Text(
        'Would You Like To Install Crafty As A Service? (Yes Or No) Note: This Can Be Done At A Later Date By Running service.bat')],
              [sg.InputText()],
              [sg.Submit()]]

    window = sg.Window('Service?', layout)
    window.Finalize()
    window.TKroot.focus_force()
    event, values = window.read()
    window.close()

    text_input = values[0]
    text_input = text_input.lower()
    service = text_input

    DirCheck()
def DirCheck():
    global path
    global remote_url
    global branch
    if os.path.exists(path) and os.path.isdir(path):
        if not os.listdir(path):
            clone()
        else:
            layout = [[sg.Text('The Directory You Entered Is Not Empty! Please Enter A Different Directory Or Delete The Contents Of The Previously Selected One!')]]

            window = sg.Window('Directory Is Not Empty!', layout)
            window.Finalize()
            window.TKroot.focus_force()
            time.sleep(5)
            window.close()
            GUI()
    else:
        os.makedirs(path)
        clone()
remote_url = 'https://gitlab.com/crafty-controller/crafty-web.git'
path = ''
branch = ''
service = ''
try:
    import pygit2
    from pathlib import Path
    import PySimpleGUI as sg
    GUI()
except ImportError:
    command_list = [sys.executable, "-m", "pip", "install", "pygit2"]
    with subprocess.Popen(command_list, stdout=subprocess.PIPE) as proc:
        print(proc.stdout.read())
    command_list = [sys.executable, "-m", "pip", "install", "pathlib"]
    with subprocess.Popen(command_list, stdout=subprocess.PIPE) as proc:
        print(proc.stdout.read())
    command_list = [sys.executable, "-m", "pip", "install", "PySimpleGUI"]
    with subprocess.Popen(command_list, stdout=subprocess.PIPE) as proc:
        print(proc.stdout.read())
    import pygit2
    from pathlib import Path
    import PySimpleGUI as sg
    GUI()


