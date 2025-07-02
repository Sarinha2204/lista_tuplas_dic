'''Implemente uma fun¸c˜ao que gire os elementos de uma lista N posi¸c˜oes para a direita'''

def girar_lista(lista, n):
    n = n % len(lista)  
    return lista[-n:] + lista[:-n]

lista_exemplo = [1, 2, 3, 4, 5] 
n = 2
resultado = girar_lista(lista_exemplo, n)
print(f"Lista original: {lista_exemplo}")
print(f"Lista girada {n} posi¸c˜oes para a direita: {resultado}")