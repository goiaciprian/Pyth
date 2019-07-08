

class Dreptunghi:
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def area():
        return self.lungime * self.latime


class Patrat(Dreptunghi):
    def __init__(self, lungime):
        super().__init__(lungime, lungime)  # ????


d = Dreptunghi(1, 2)
print(d.area)

p = Patrat(1)
print(p.area())  # ????
