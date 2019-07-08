#!usr/bin/env python3

from sys import platform
from subprocess import Popen
from subprocess import PIPE
from subprocess import CalledProcessError


def windows():
    import os
    PATH = r"C:\Users\camio\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\PbInfo.lnk"
    os.startfile(PATH)


def linux():
    commands = 'explorer.exe PbInfo.lnk'
    process = Popen('/bin/bash', stdin=PIPE, stdout=PIPE, shell=True,
                    cwd="/mnt/c/Users/camio/AppData/Roaming/Microsoft/Windows/Start Menu/Programs")
    out, err = process.communicate(commands.encode('utf-8'))


if __name__ == "__main__":
    if platform == "win32":
        windows()
    else:
        linux()
