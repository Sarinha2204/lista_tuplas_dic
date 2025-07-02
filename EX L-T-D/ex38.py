'''Implemente uma fun¸c˜ao que receba uma lista e retorne os elementos na ordem
inversa.'''


def ordem_inversa(lista):
    return lista[::-1]

lista = [10, 20, 30, 40, 50]
lista_invertida = ordem_inversa(lista)

print("Lista original:", lista)
print("Lista invertida:", lista_invertida)
