

class Meta(type):
    def __new__(cls, name, base, dct):
        x = super().__new__(cls, name, base, dct)
        x.attr = 100
        return x


class Foo(metaclass=Meta):
    pass

x = Foo()

print(type(x))
print(x)

print(x.__class__)
print(x.__class__.__dict__)
