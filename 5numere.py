
def max_list(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max


count, lista = 0, []

while count < 5:
    try:
        numere = int(input('::'))
    except ValueError:
        continue
    else:
        lista.append(numere)
        count += 1


the3 = []

while count < 8:
    max = max_list(lista)
    the3.append(max)
    lista.remove(max)
    count += 1

print(sum(the3))
