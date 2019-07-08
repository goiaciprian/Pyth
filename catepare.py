
lista = []
while True:
    try:
        numere = int(input('::'))
    except ValueError:
        continue
    else:
        if numere == 0:
            if len(lista):
                print(len(lista))
            else:
                print(lista)
                print('Nu au fost numere pare')
            break
        elif numere % 2 == 0:
            lista.append(numere)