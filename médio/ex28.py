'''Crie uma fun¸c˜ao que receba uma lista e retorne a soma de todos os elementos
num´ericos.'''

def soma_numericos(lista):
    soma = 0
    for item in lista:
            soma += item
    return soma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(soma_numericos(lista))

