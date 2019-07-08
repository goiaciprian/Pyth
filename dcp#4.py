#!usr/bin/env python
import re


def absolutePath(fullpath: str):
    splitTerm, fisier = "\n\t", ''
    folders = re.split(splitTerm, fullpath)
    for document in folders:
        if "\t" and "." in document:
            fisier = document[1::]
    return folders[0] + '\\' + folders[-2] + '\\' + fisier

if __name__ == "__main__":
    print(absolutePath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
