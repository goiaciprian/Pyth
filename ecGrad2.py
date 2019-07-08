# usr/bin/env python
import math


class EcGrad2(object):
    def __init__(self, a: int, b: int, c: int):
        if a == 0:
            print("Coeficientul lui x^2 trebuie sa fie diferit de 0.")
            quit(1)
        try:
            self.a = int(a)
            self.b = int(b)
            self.c = int(c)
        except ValueError as e:
            print(repr(e))
        self.delta = 0
        self.x1 = None
        self.x2 = None
        self.varf = None
        self.form = None
        self.prodForm = None
        self.crescatoare = None
        self.descrescatoare = None

    def __repr__(self):
        if self.b <= 0 and self.c <= 0:
            self.form = f"{self.a}x^2 {self.b}x {self.c} = 0"
        elif self.b <= 0 and self.c >= 0:
            self.form = f"{self.a}x^2 {self.b}x +{self.c} = 0"
        elif self.b >= 0 and self.c <= 0:
            self.form = f"{self.a} + {self.b}x {self.c} = 0"
        elif self.b >= 0 and self.c >= 0:
            self.form = f"{self.a} + {self.b} +{self.c} = 0"
        return f"{form},\n {self.prodForm},\n"

    def __str__(self):
        if self.b <= 0 and self.c <= 0:
            self.form = f"{self.a}x^2 {self.b}x {self.c} = 0"
        elif self.b <= 0 and self.c >= 0:
            self.form = f"{self.a}x^2 {self.b}x +{self.c} = 0"
        elif self.b >= 0 and self.c <= 0:
            self.form = f"{self.a}x^2 + {self.b}x {self.c} = 0"
        elif self.b >= 0 and self.c >= 0:
            self.form = f"{self.a}x^2 + {self.b}x +{self.c} = 0"
        if not self.x1:
            self.roots()
        return f"{self.form},\n{self.prodForm},\n"

    def __call__(self):
        self.calcDelta()
        self.roots()
        self.varfulFunctiei()
        return self.x1, self.x2, self.varf

    def calcDelta(self):
        self.delta = self.b**2 - 4*self.a*self.c
        return self.delta

    def roots(self):
        # import pdb
        # pdb.set_trace()

        if not self.delta:
            self.calcDelta()

        if self.delta is int or self.delta is float:
            pass

        x1 = (-self.b + math.sqrt(self.delta)) / 2*self.a
        x2 = (-self.b - math.sqrt(self.delta)) / 2*self.a

        intX = str(x1)  # this can either be x1 or x2

        if x1 == x2 and x1 < 0:
            self.prodForm = f"{self.a}(x + {intX[1::]})^2"
        elif x1 == x2 and x1 > 0:
            self.prodForm = f"{self.a}(x - {x1})^2 "
        else:
            if x1 > 0 and x2 > 0:
                self.prodForm = f"{self.a}(x - {x1})(x - {x2})"
            elif x1 > 0 and x2 < 0:
                self.prodForm = f"{self.a}(x - {x1})(x + {x2})"
            elif x1 < 0 and x2 > 0:
                self.prodForm = f"{self.a}(x + {x1})(x - {x2})"
            elif x1 < 0 and x2 < 0:
                self.prodForm = f"{self.a}(x + {x1})(x + {x2})"

        self.x1 = x1
        self.x2 = x2

        return x1, x2

    def varfulFunctiei(self):
        punctX = -self.b/2*self.a
        if not self.delta:
            self.delta()
        punctY = -self.delta/4*self.a
        self.varf = (punctX, punctY)
        return (punctX, punctY)

    def monotonie(self):
        if not self.varf:
            self.varfulFunctiei()
        if self.a > 0:
            self.crescatoare = f"[{self.varf[0]}, + infinit)"
            self.descrescatoare = f"(- infinit, {self.varf[0]}]"
        elif self.a < 0:
            self.descrescatoare = f"[{self.varf[0]}, + infinit)"
            self.crescatoare = f"(- infinit, {self.varf[0]}]"


if __name__ == "__main__":
    import sys
    coef = sys.argv
    functie = EcGrad2(coef[1], coef[2], coef[3])
    print(functie)
