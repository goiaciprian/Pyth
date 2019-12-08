import os


"""

statisticiordine.in content:
6 4(k)
1 58 4 3 50 24

Citeste un fisier si gseste al k-lea cel mai mic element si creeaza un fisier
statisticiordine.out cu acel element.(in cazul de mai sus 24.)

"""


def dec_out(functie):

    def wraper():
        rasp = functie()
        with open('statisticiordine.out', 'w') as outfile:
            outfile.write(rasp)
        return
    return wraper


@dec_out
def func():
    """
    :return int: the k smallest number
    """
    with open('statisticiordine.in', 'r') as infile:
        content = infile.read()
        content = content.split()
    n = content[0]
    k = content[1]
    content.remove(n)
    content.remove(k)

    count = 0
    minim = None
    while count < 2:
        minim = min(content)
        print(minim)
        content.remove(minim)
        print(content)
        count += 1
    return minim


if __name__ == "__main__":
    assert os.path.isfile('statisticiordine.in'), "There's not such file."
    func()
