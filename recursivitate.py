#!usr/bin/env python3


def recFunc(x: int):
    x -= 1
    if x == 0:
        print('gata')
    else:
        print('inca nu')
        recFunc(x)w


if __name__ == "__main__":
    import random
    lista = [1, 2, 3, 4, 5, 6, 7]
    recFunc(12)
