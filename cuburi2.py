#!usr/bin/env python

"""

CEL MAI GREU DE PANA ACUM

Gigel are un set de n cuburi. Fiecare cub este marcat cu un număr natural, de
la 1 la n și i se cunoaște lungimea laturii – număr natural. Cu o parte dintre
 aceste cuburi Gigel va construi o stivă, astfel:

fiecare cub se analizează o singură dată, în ordinea numerelor marcate;
dacă stiva nu conține niciun cub, cubul curent devine baza stivei
dacă cubul curent are latura mai mică sau egală cu cubul din vârful stivei,
se adaugă pe stivă; dacă cubul curent are latura mai mare decât cubul din
vârful stivei, se vor înlătura de pe stivă cuburi (eventual toate) până când
cubul curent are latura mai mică sau egală cu cubul din vârful stivei.
Să se afișeze numerele de pe cuburile existente la final în stivă, de
la bază spre vârf.

Date de intrare
Programul citește de la tastatură numărul n, apoi n numere naturale,
reprezentând, în ordine, lungimile laturilor cuburilor.

Date de ieșire
Programul va afișa pe ecran numărul de cuburi existente pe stivă, iar pe linia
următoare, separate prin câte un spațiu, numerele marcate pe aceste cuburi.

Restricții și precizări
1 ≤ n ≤ 1000
lungimile cuburilor vor fi mai mici decât 1000

Exemplu
Intrare

6
7 4 3 5 1 2

Ieșire

3
1 4 6

"""

while True:
    try:
        global n
        n = int(input('::'))
    except ValueError as e:
        print(e)
    else:
        break

sir, stiva = [], []

while not sir:
    sirInp = input('::')
    if len(sirInp) == (n*2-1):
        sir.append(sirInp)
    else:
        print('Elemente insuficiente.')

sir = sir[0].split()

if not stiva:
    stiva.append('7')


for n, i in enumerate(sir[1::]):
    # import pdb; pdb.set_trace()
    last = stiva[len(stiva)-1]
    for l in reversed(stiva):
        if int(i) > int(last):
            elem = stiva[len(stiva)-1]
            stiva.remove(elem)
            last = stiva[len(stiva)-1]
        else:
            stiva.append(i)
            break

print(len(stiva))
for cubBun in stiva:
    for index, cub in enumerate(sir):
        if cubBun == cub:
            print(str(index+1), end=' ')
