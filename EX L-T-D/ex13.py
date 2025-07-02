'''Crie uma lista com os números de 1 a 10 usando range() e imprima somente os
pares.'''

num = list(range(1, 11))

for numeros in num:
    if numeros % 2 == 0:
        print(numeros)