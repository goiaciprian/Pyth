#!usr/bin/env python


class Stiva(list):
    def __init__(self):
        list.__init__(self)
        self._stiva = []

    def push(self, x):
        self._stiva.append(x)

    def pop(self):
        if len(self._stiva) != 0:
            return self._stiva[len(self._stiva) - 1]
        else:
            pass

    def top(self):
        if len(self._stiva) != 0:
            return self._stiva[len(self._stiva) - 1]


if __name__ == "__main__":
    from random import randint
    stiva = Stiva()
    while True:
        try:
            user = int(input('::'))
        except ValueError as e:
            print(e)
        else:
            global times
            times = user
            break

    count = 0

    while count < times:
        pick = randint(1, 3)
        if pick == 1:
            number = randint(-100, 100)
            stiva.push(number)
        elif pick == 2:
            stiva.pop()
        else:
            print(stiva.top())
        count += 1
