'''Implemente uma fun¸c˜ao que conte quantas vezes um valor aparece em uma lista.'''



def contar_ocorrencias(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador

lista = [1, 2, 3, 2, 4, 2, 5]
valor = 2
print(contar_ocorrencias(lista, valor))