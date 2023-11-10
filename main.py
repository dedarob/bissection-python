import math

errorMarg = float(input("Digite a margem de erro (ex: 0.01):\n"))

# Encontrar f(x) = x² + ln(x) por bisseção

a = 0.5
b = 1
c = (a + b) / 2

funcA = a**2 + math.log(a)
funcB = b**2 + math.log(b)
if funcA * funcB > 0:
    print("Função não tem raiz.")
    exit()
else:
    while (b - a) >= errorMarg:
        funcA = a**2 + math.log(a)
        funcB = b**2 + math.log(b)
        funcC = c**2 + math.log(c)
        if funcA * funcC > 0:
            a = c
        if funcB * funcC > 0:
            b = c
        c = (a + b) / 2
    result = (a + b) / 2
    print("Resultado: {:.4}".format(result))