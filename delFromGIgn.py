#!/usr/bin/env python3.7

import os
from os import remove
from sys import platform


_PATH = None  # the folder where we want to delete the files
_DELFROM = None  # the file containg the name of the files that we want to delete
_LINUX = False


def delProcess(path: str, delFrom: str, linux: bool = False) -> None:

    __file = None
    __content = None
    __deleteElements = []

    if (linux):
        if (path[len(path)::] != '/'):
            path += '/'

    else:
        if (path[len(path)::] != "\\"):
            path += "\\"

    __file = str(path + delFrom)

    assert os.path.isfile(__file), "There was no file"

    with open(__file, 'r') as file:
        __content = file.read()
        __deleteElements = __content.split("\n")
        del __content

    print("Starting the removing process... \n")

    for i in __deleteElements:
        temp = path + i

        # ! No, aici crapa dupa ce sterge toate fisierele =)))
        # TODO Sa nu mai crape dupa ce termina de sters fisierele
        # ?? O alta varianta ar fii sa folosesc system in loc de os.remove
        # * system(Remove-Item path) -> powershell
        # * rm path -> terminal
        try:
            remove(temp)
        except ModuleNotFoundError:
            print("An error occured -> Moving on....")
        except IsADirectoryError:
            print("An error occured -> Moving on....")
        except FileNotFoundError:
            print("An error occured -> Moving on....")

        else:
            print("Removing " + i + ".....DONE")
    else:
        del temp


if __name__ == "__main__":

    _PATH = str(input("PATH to the folder: "))
    _DELFROM = str(input("DELFROM file name: "))

    if (platform != 'win32'):
        _LINUX = True
        pathElements = _PATH.split("\\")
        _PATH = ""
        pathElements[0] = f"/mnt/{pathElements[0][:1].lower()}"
        for i in pathElements:
            if (i != pathElements[0]):
                _PATH += '/' + i
            else:
                _PATH += i

        del pathElements
        del i

    delProcess(_PATH, _DELFROM, linux=_LINUX)
