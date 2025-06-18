'''FILTER: filtra os itens de um iterável com base em uma função que retorna True ou 
False, retornando um novo iterável com os itens que passaram no teste.'''

#Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6]

