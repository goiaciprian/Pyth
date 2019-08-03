#!/usr/bin/env python3

from PyPDF2 import PdfFileReader
from sys import argv

from pdb import set_trace


def openFile(path: str) -> str:
    # set_trace()
    with open(path, 'rb') as file:
        fileReader = PdfFileReader(file)
        pageObject = fileReader.getPage(0)
        content = pageObject.extractText()
        return content

if __name__ == "__main__":
    try:
        contentfile1 = openFile(argv[1])
        print(contentfile1)
    except Exception as e:
        print(e)
