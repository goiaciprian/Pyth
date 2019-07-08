#!usr/bin/env python

userchoice = []
count = 0
while count < 2:
    user = input("Introdu un numar:")
    if user == 'q':
        exit(1)
    try:
        user = int(user)
    except ValueError:
        print('Introduceti numai numere')
        continue
    userchoice.append(user)
    count += 1

print(pow(userchoice[0], userchoice[1]))
