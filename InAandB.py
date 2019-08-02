#!/usr/bin/env python3

from PyPDF2 import PdfFileReader
from sys import argv

from pdb import set_trace

def openFile(path: str) -> str:
    # set_trace()
    file = open(path, 'rb')
    content = file.read()
    fileReader = PdfFileReader(file)
    secondContent = fileReader.read(file)
    try:
        return secondContent
    finally:
        file.close()

if __name__ == "__main__":
    contentfile1 = openFile(argv[1])
    print(contentfile1)