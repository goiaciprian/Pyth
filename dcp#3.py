#!usr/bin/env python

"""

Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain duplicates
and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
should give 3.

"""


def maxNumber(array: list):
    max = 0
    for i in array:
        if i > max:
            max = i
    return max


def minNumber(array: list):
    minim = maxNumber(array)
    for i in array:
        if i < minim:
            minim = i
    return minim


def lowestPositive(array: list):
    posibilitati = range(minNumber(array), maxNumber(array)+1)
    param = maxNumber(array)
    for i in posibilitati:
        if i not in array and i < param and i != 0:
            param = i
    return param

if __name__ == "__main__":
    print(lowestPositive([3, 4, -1, 1]))
