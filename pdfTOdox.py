# usr/bin/env python3

import sys
import os


def getPDF(abs_path: str) -> str:
    with open(abs_path, 'r+') as pdf:
        content = pdf.read()


def writeDOCx(abs_path: str, content: str) -> bool:
    if abs_path == '.':
        abs_path = os.path.dirname(os.path.realpath(__file__)) + '\doc' \
                                                                 'ument.docx'
    with open(abs_path, 'w+') as docx:
        import pdb; pdb.set_trace()
        if docx.writable():
            try:
                docx.write(content)
            except Exception:
                return False
            else:
                return True
        else:
            return False


def main():
    argm = sys.argv
    text = getPDF(argm[1])
    if argm.__len__() == 2:
        writeDOCx(argm[2], text)
    else:
        writeDOCx('.', content=text)


if __name__ == "__main__":
    main()
