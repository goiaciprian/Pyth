#!usr/bin/env python

"""

Cerința

Săturat de ținut uși, Hodor s-a hotărât să devină ceasornicar.
Maestrul ceasornicar îi spune lui Hodor că îl va învăța, doar
dacă va trece un test. Maestrul îi da lui Hodor un sistem de
coordonate xOy, și un ceas cu raza r, al cărui centru se află
în centrul sistemului de coordonate O(0,0). Ceasul contine doar
limba care indica orele, de lungime r. Inițial limba indică ora
12:00, cu vârful în punctul de coordonate A(0,r). Hodor trebuie
să afle coordonatele vârfului limbii, după h ore și m minute.

Date de intrare

Fișierul de intrare ceas.in conține pe prima linie trei numere
naturale r, h, m, separate prin câte un spațiu, cu semnificațiile
din enunț.

Date de ieșire

Fișierul de ieșire ceas.out va conține pe prima linie două numere
x, y, reprezentând coordonatele vârfului limbii ceasului după h
ore și m minute.

Restricții și precizări

1 ≤ r ≤ 100
0 ≤ h ≤ 11
0 ≤ m ≤ 59
coordonatele vor fi punctate dacă diferența dintre cele afișate
de program și cele corecte este mai mică decât 0.01.

Exemplu

ceas.in
33 6 0

ceas.out
0.000 -33.000

"""

while True:
    try:
        global raza
        raza = int(input('Raza '))
    except ValueError as e:
        print(e)
    else:
        break

while True:
    try:
        global ore
        ore = int(input('Ore '))
    except ValueError as e:
        print(e)
    else:
        break

while True:
    try:
        global minute
        minute = int(input('Minute '))
    except ValueError as e:
        print(e)
    else:
        break

timpTotal, countTimp = ore * 60 + minute, 0
varfLimba, treime = [0, raza], raza / 3
perMinutRow = treime / 60
perMinut = round(perMinutRow, 1)
ora = {
    12: [0, raza],
    1: [treime, raza-treime],
    2: [2*treime, raza-2*treime],
    3: [raza, 0],
    4: [raza-treime, -treime],
    5: [raza-2*treime, -2*treime],
    6: [0, -raza],
    7: [-treime, -raza+treime],
    8: [-2*treime, -raza+2*treime],
    9: [-raza, 0],
    10: [-raza+treime, treime],
    11: [-raza+2*treime, 2*treime]
}

# while countTimp < timpTotal:
#     if varfLimba[1] >= raza:
#         count = 0
#         while cout < 60:
#             varfLimba[0] += perMinut
#             varfLimba[1] -= perMinut
#     elif 0 < varfLimba[1] < 1:
#         count = 0
#         while cout < 60:
#             varfLimba[0] -= perMinut
#             varfLimba[1] += perMinut
#     elif 


# Merge daca variabila perMinut este numar intreag 
while countTimp < timpTotal:
    if ora[12] <= varfLimba <= ora[3]:
        count = 0
        while count < 60:
            varfLimba[0] += perMinut
            varfLimba[1] -= perMinut
            count += 1
            countTimp += 1
    elif ora[3] <= varfLimba <= ora[6]:
        count = 0
        while count < 60:
            varfLimba[0] -= perMinut
            varfLimba[1] += perMinut
            count += 1
            countTimp += 1
    elif ora[6] <= varfLimba <= ora[9]:
        count = 0
        while count < 60:
            varfLimba[0] += perMinut
            varfLimba[1] -= perMinut
            count += 1
            countTimp += 1
    elif ora[9] <= varfLimba <= ora[12]:
        count = 0
        while count < 60:
            varfLimba[0] -= perMinut
            varfLimba[1] += perMinut
            count += 1


# Merge 100 %
# while countTimp < timpTotal:
#     if varfLimba == ore[12]:
#         varfLimba = ore[1]
#         countTimp += 60
#     elif varfLimba == ore[1]:
#         varfLimba = ore[2]
#         countTimp += 60
#     elif varfLimba == ore[2]:
#         varfLimba = ore[3]
#         countTimp += 60
#     elif varfLimba == ore[3]:
#         varfLimba = ore[4]
#         countTimp += 60
#     elif varfLimba == ore[4]:
#         varfLimba = ore[5]
#         countTimp += 60
#     elif varfLimba == ore[5]:
#         varfLimba = ore[6]
#         countTimp += 60
#     elif varfLimba == ore[6]:
#         varfLimba = ore[7]
#         countTimp += 60
#     elif varfLimba == ore[7]:
#         varfLimba = ore[8]
#         countTimp += 60
#     elif varfLimba == ore[8]:
#         varfLimba = ore[9]
#         countTimp += 60
#     elif varfLimba == ore[9]:
#         varfLimba = ore[10]
#         count += 60
#     elif varfLimba == ore[10]:
#         varfLimba = ore[11]
#         count += 60

for i in varfLimba:
    print(i, end=' ')
