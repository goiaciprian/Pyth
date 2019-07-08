#!usr/bin/env python

'''
Eroul nostru, Căldărușe, are un număr n de cărți pe care le are aranjate una peste cealaltă (sub forma unui stack). 
Cartea din vârf are valoarea a1, următoarea a2 și așa mai departe. Cartea de la bază are indicele n (an). 
Toate numerele sunt distincte.

Căldărușe vrea să mute toate cărțile în ghiozdanul lui în exact n pași. În timpul pasului de ordin i, 
el vrea să mute cartea cu numărul bi în ghiozdan. Dacă această carte se află în stack, el o ia atât pe ea, 
cât și toate cărțile situate deasupra acesteia și le pune în ghiozdan; în caz contrar, el nu va face nimic și 
va trece la următorul pas. De exemplu, dacă în stack cărțile sunt aranjate în ordinea [1, 2, 3] 
(cartea cu numărul 1 este aflată în vârf) și pașii prin care Căldărușe trece sunt, în această ordine, 
[2, 1, 3], atunci în cadrul primului pas el va muta două cărți (1 și 2), în cadrul celui de-al doilea pas 
nu va face nimic (din moment ce cartea cu numărul 1 este deja în ghiozdan) și în cadrul ultimului pas 
va muta o singură carte (cartea cu numărul 3).

Date de intrare

Prima linie va conține numărul n, cu semnificația din enunț. Următoarea linie va conține n numere 
întregi, anume a1,a2,…,an. A treia linie va conține alte n numere întregi, anume b1,b2,…,bn.

Date de ieșire

Programul va afișa pe ecran n numere întregi. Elementul de ordine i ar trebui să fie egal cu numărul de 
cărți pe care Căldărușe le mută în ghiozdanul său în timpul pasului i.

Exemple:
Intrare

3
1 2 3
2 1 3

Ieșire

2 0 1

'''

nrpasi, count, siruri = 0, 0, []

while True:
    try:
        user = int(input('::'))
    except ValueError as e:
        print(e)
    else:
        nrpasi = user
        break

while count < 2:
    sir = input('::')
    if len(sir) == (nrpasi*2 - 1):
        siruri.append(sir)
        count += 1
    else:
        print(f'Nu sunt {nrpasi} elemente in sir.')

lista_carti, lista_pasi, raspuns = siruri[0].split(), siruri[1].split(), []

for l in lista_pasi:
    if l in lista_carti:
        for index, zb in enumerate(lista_carti):
            if l == zb:
                nrcarti = index
                break
        lungime, count2 = 0, 0
        for i in lista_carti[0:nrcarti+1]:
            lungime += 1
        while count2 < lungime:
            lista_carti.pop(0)
            count2 += 1
        raspuns.append(lungime)
    else:
        raspuns.append(0)

for i in raspuns:
    print(i, end=' ')
