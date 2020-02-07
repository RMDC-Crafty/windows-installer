import os
import time
try:
    import pygit2
    from pathlib import Path
    import PySimpleGUI as sg
except ImportError:
    command_list = [sys.executable, "-m", "pip", "install", "pygit2"]
    with subprocess.Popen(command_list, stdout=subprocess.PIPE) as proc:
        print(proc.stdout.read())
    command_list = [sys.executable, "-m", "pip", "install", "pathlib"]
    with subprocess.Popen(command_list, stdout=subprocess.PIPE) as proc:
        print(proc.stdout.read())
    import pygit2
    from pathlib import Path
remote_url = 'https://gitlab.com/crafty-controller/crafty-web.git'
path = ''
branch = ''

def clone(remote_url, path, branch):
    """Clone a repo in a give path and update the working directory with
    a checkout to head (GIT_CHECKOUT_SAFE_CREATE)

    :param str remote_url: URL of the repository to clone

    :param str path: Local path to clone into

    :param str branch: Branch to checkout after the
    clone. The default is to use the remote's default branch.

    """
    repo = pygit2.clone_repository(remote_url, path, checkout_branch=branch)
    repo.checkout_head()
    data_folder = Path(path)
    file_to_open = data_folder / "run_crafty.bat"
    reqfile_to_open = data_folder / "requirements.txt"
    file = open(file_to_open, "w")
    file.write("python crafty.py")
    file.close()
    file_to_open = data_folder / "run_crafty_verbose.bat"
    file = open(file_to_open, "w")
    file.write("python crafty.py -v")
    file.close()
    import subprocess
    import sys
    file = open(reqfile_to_open, "r")

    for line in file:
        req = line.split("/n")
        command_list = [sys.executable, "-m", "pip", "install", req]
        with subprocess.Popen(command_list, stdout=subprocess.PIPE) as proc:
            print(proc.stdout.read())

def GUI():
    global remote_url
    global path
    global branch
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
    if len(os.listdir(path)) == 0:
        clone(remote_url, path, branch)
    else:
        layout = [[sg.Text('The Directory You Entered Is Not Empty!, Please Enter A Different Directory.')]]

        window = sg.Window('Directory Is Not Empty!', layout)
        window.Finalize()
        window.TKroot.focus_force()
        time.sleep(5)
        window.close()
        GUI()
GUI()
