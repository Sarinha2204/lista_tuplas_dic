'''Crie uma função que recebe uma lista e retorna uma nova lista com apenas os
elementos únicos.'''

def elementos_unicos(lista):
    unicos = []
    for item in lista:
        if item not in unicos:
            unicos.append(item)
    return unicos

numeros = [1, 2, 2, 3, 4, 4, 5]
resultado = elementos_unicos(numeros)
print(resultado)
