'''Implemente a busca bin´aria em uma lista ordenada.'''
def busca_binaria(lista, valor):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio  
        elif lista[meio] < valor:
            esquerda = meio + 1  
        else:
            direita = meio - 1  
    return -1  

lista_exemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
valor_procurado = 7
resultado = busca_binaria(lista_exemplo, valor_procurado)
if resultado != -1:
    print(f"Valor {valor_procurado} encontrado no índice {resultado}.")