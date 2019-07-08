#!usr/bin/env python

"""

Subprogramul duplicare are un singur parametru, n, prin care primește un număr natural (n∈[1,104)).
Subprogramul furnizează, prin același parametru, numărul obținut din n prin inserarea, după fiecare 
cifră pară din scrierea lui, a unei cifre egale cu jumătate din aceasta.

Exemplu:

Dacă n=2380 după apel, n=2138400, iar dacă n=35 după apel, n=35.

"""

def duplicare(n: int) -> int:
    """
    :param int n: enter a number
    :return str: return the numbers plus the half of the prime numbers after them
    """
    returnvar = str(n)
    truereturn = ''
    for i in returnvar:
        if int(i) % 2 == 0:
            half = int(int(i) / 2)
            add = i + str(half)
            truereturn += add
        else:
            truereturn += i
    return int(truereturn)

if __name__ == "__main__":
    print(duplicare(2380))
