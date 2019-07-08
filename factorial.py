
def factorial(n):
    numere, rezultat = [x for x in range(1, n+1)], 1
    if n == 0:
        return 1
    else:
        for i in numere:
            rezultat *= i
    return rezultat

print(factorial(4))
