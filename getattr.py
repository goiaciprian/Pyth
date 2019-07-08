#!usr/bin/env python


class Animal:
    def __init__(self, name=None):
        self.name = name

    def bark(self):
        return f'{self.name} barks.' if self.name else 'My animal barks.'

    def poop(self):
        return f'{self.name} poops.' if self.name else 'My animal poops.'


class Dog:
    def __init__(self, name=None):
        self.name = name

    def bark(self):
        return f'{self.name} barks.' if self.name else 'My dog barks.'
if __name__ == "__main__":
    if hasattr(Animal, 'poop'):
        a = getattr(Animal(), 'poop')
    if hasattr(Dog, 'bark'):
        b = Dog()
    print(getattr(b, 'bark'))
    print(a())
