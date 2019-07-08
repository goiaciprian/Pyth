import string

mesajcriptat = ''
alfabet = string.ascii_lowercase
lista_alfabet = [x for x in alfabet]

cuvant = input('::').lower()

while True:
    try:
        key = int(input('::'))
    except ValueError:
        continue
    else:
        global cheie
        cheie = key
        break

for index, litera in enumerate(cuvant):
    if litera in alfabet:
        pozitie = alfabet.find(litera)
        pozitie_noua = (pozitie + key) % 26
        for n, k in enumerate(lista_alfabet):
            litera_noua = lista_alfabet[pozitie_noua]
            if litera_noua in mesajcriptat:
                continue
            else:
                mesajcriptat += litera_noua
    else:
        mesajcriptat += litera

print(mesajcriptat)
