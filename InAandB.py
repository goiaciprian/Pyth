#!/usr/bin/env python3

from PyPDF2 import PdfFileReader
from sys import argv

from pdb import set_trace


def openFile(path: str) -> str:
    # set_trace()
    content = ''
    file = open(path, 'rb')
    fileReader = PdfFileReader(file)
    for i in range(0, fileReader.getNumPages()):
        pageObject = fileReader.getPage(i)
        content += pageObject.extractText()
        print(content)
    try:
        return content
    finally:
        file.close()

if __name__ == "__main__":
    try:
        contentfile1 = openFile(argv[1])
        print(contentfile1)
    except Exception as e:
        print(e)
