'''Implemente a fun¸c˜ao zip manualmente (como em zip(lista1, lista2)).'''

def zip_manual(lista1, lista2):
    tamanho_minimo = min(len(lista1), len(lista2))
    resultado = []
    for i in range(tamanho_minimo):
        resultado.append((lista1[i], lista2[i]))
    return resultado

lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
resultado = zip_manual(lista1, lista2)
print(f"Lista 1: {lista1}")