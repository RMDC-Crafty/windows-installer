try:
    import pygit2
    from pathlib import Path
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
path = input('Where Would You Like Crafty To Install To?')
branch = input('What Branch Would You Like To Clone? Choose From: "Master", "Dev", "Snapshot" And "Beta".')
branch = branch.lower()


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


clone(remote_url, path, branch)
