import intervals as I

count, lista = 0, []
while count < 3:
    try:
        numbers = int(input('::'))
    except ValueError:
        continue
    else:
        lista.append(numbers)
        count += 1

if lista[2] in I.closed(lista[0], lista[1]):
    print('DA')
else:
    print('NU')
