'''Dada uma lista de n´umeros, retorne uma nova lista com os elementos ao quadrado,
mas somente os pares.'''

def quadrado_pares(lista):
    return [x ** 2 for x in lista if x % 2 == 0]

lista_exemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = quadrado_pares(lista_exemplo)
print(f"Lista original: {lista_exemplo}")
print(f"Ao quadrado: {resultado}")