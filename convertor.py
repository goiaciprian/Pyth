#!/usr/bin/env python3

from sys import argv


def convertor(curs, sumaBani)-> dict:
    sumaTotal = curs * sumaBani
    lei = sumaTotal
    banc50, banc10, banc5, banc1 = 0, 0, 0, 0

    if (sumaTotal >= 50):
        banc50 = int(sumaTotal / 50)
        sumaTotal -= banc50 * 50

    if (sumaTotal >= 10):
        banc10 = int(sumaTotal / 10)
        sumaTotal -= banc10 * 10

    if (sumaTotal >= 5):
        banc5 = int(sumaTotal / 5)
        sumaTotal -= banc5 * 5
    else:
        banc1 = sumaTotal

    return {
        "curs": curs,
        "Euro": sumaBani,
        "Lei": lei,
        "Ron": (lei * 10),
        "Bancnota 50": banc50,
        "Bancnota 10": banc10,
        "Bancnota  5": banc5,
        "Bancnota  1": banc1
    }


if __name__ == "__main__":
    curs = float(argv[1])
    n = int(argv[2])

    with open("C:\\Users\\camio\\Desktop\\numere.txt", "w+") as file:
        for i in range(100, n + 1, 100):
            # print("Pentru: " + str(i) + "\n")
            file.write("Pentru: " + str(i) + "\n\n")
            for i, j in convertor(curs, i).items():
                # print(str(i) + ": " + str(j))
                file.write(str(i) + ": " + str(j) + "\n")
            # print("\n")
            file.write("\n")
