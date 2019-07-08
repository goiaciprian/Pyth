# usr/bin/env python
# -*- coding: utf-8 -*-


def mediaGeometrica(putere: int, numere: str or list):
    if type(numere) == str:
        listaNumere = [int(i) for i in numere if i != ' ']
        produs = 1
        for i in listaNumere:
            produs *= i
        return pow(produs, 1/putere)

    elif type(numere) == list:
        produs = 1
        for i in numere:
            produs *= i
        return pow(produs, 1/putere)

if __name__ == "__main__":
    print(mediaGeometrica(3, '3 3 3'))
