'''Divida uma lista em N sublistas de tamanho igual'''
def dividir_lista(lista, n):
    if n <= 0:
        raise ValueError("O número de sublistas deve ser maior que zero.")
    
    tamanho_sublista = len(lista) // n
    sublistas = []
    
    for i in range(n):
        inicio = i * tamanho_sublista
        fim = inicio + tamanho_sublista
        sublistas.append(lista[inicio:fim])
    
    if len(lista) % n != 0:
        sublistas[-1].extend(lista[n * tamanho_sublista:])
    
    return sublistas

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
resultado = dividir_lista(lista, n)
print(f"Lista original: {lista}")
print(f"Dividida em {n} sublistas: {resultado}")
