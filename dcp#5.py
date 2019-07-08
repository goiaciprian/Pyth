#!usr/bin/env python
# coding: utf-8


def unique(array: list):
    arrayDict = {str(x): 0 for x in array}
    for x in array:
        arrayDict[str(x)] += 1
    for x, y in arrayDict.items():
        if y == 1:
            print(arrayDict[x])

if __name__ == "__main__":
    unique([6, 1, 3, 3, 3, 6, 6])
