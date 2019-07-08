#!usr/bin/env python

"""

Determinați valoarea unor anumiți biți din reprezentarea sa internă.

"""

while True:
    try:
        global numar
        global max_num
        numar, max_num = int(input('::')), int(input('::'))
    except ValueError as e:
        print(e)
    else:
        break

reprezentari = []

while not reprezentari:
    elem_de_repr = input('::')
    lista_cu_repr = elem_de_repr.split()
    for i in lista_cu_repr:
        if len(reprezentari) <= max_num:
            reprezentari.append(i)

numar_bits = bin(numar)  # 64 bit number is unknown with out a library >
# microsoft visual c++ 14.0 error when i install
# gimpy2 or bitarray
