'''Separe uma lista de n´umeros em duas: uma com pares e outra com ´ımpares.'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []

for listas in lista:
    if listas % 2 == 0:
        pares.append(listas)
    else:
        impares.append(listas)
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")