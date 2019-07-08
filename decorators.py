
def input_decorator(func):
    def user_input():
        while True:
            try:
                numere = int(input('::'))
            except ValueError:
                continue
            else:
                func(numere)
                break
    return user_input


@input_decorator
def hi(numere: str=4):
    print(f'Numarul este {numere}.')

hi()
