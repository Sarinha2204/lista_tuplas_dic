''' Dada uma lista de valores, encontre todos os pares que somam exatamente 10'''

def encontrar_pares_soma_10(lista):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == 10:
                pares.append((lista[i], lista[j]))
    return pares

lista_exemplo = [1, 2, 3, 7, 8, 5, 4, 6]
resultado = encontrar_pares_soma_10(lista_exemplo)
print(f"Lista original: {lista_exemplo}")
print(f"Pares que somam 10: {resultado}")