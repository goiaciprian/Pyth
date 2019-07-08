#!usr/bin/env python

"""

Reguli:

1 Cifra 2 se poate înlocui cu succesiunea:  12(n ori)
2 Cifra 3 se poate înlocui cu succesiunea:  03(k ori)
3 Cifra 2 se poate înlocui cu succesiunea:  01(o data)
4 Cifra 3 se poate înlocui cu succesiunea:  10(o data)

Verificare:

Pentru 5 4 rezultatul este 1111101000010.

"""

while True:
    try:
        n_input = int(input('::'))
    except ValueError as e:
        print(e)
    else:
        global n
        n = n_input
        break

while True:
    try:
        k_input = int(input('::'))
    except ValueError as e:
        print(e)    
    else:
        global k
        k = k_input
        break

start, count = '23', 0

while count < n:
    for e in start:
        if e == '2':
            start = start.replace('2', '12', 1)
    count += 1
else:
    count = 0

while count < k:
    for e in start:
        if e == '3':
            start = start.replace('3', '03', 1)
    count += 1
else:
    count = 0

while count < 1:
    for e in start:
        if e == '2':
            start = start.replace('2', '01', 1)
    count += 1
else:
    count = 0

while count < 1:
    for e in start:
        if e == '3':
            start = start.replace('3', '10', 1)
    count += 1

print(start)
