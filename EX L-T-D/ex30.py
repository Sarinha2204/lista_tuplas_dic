'''Dada uma lista de strings, crie uma nova lista com o tamanho (número de caracteres)
de cada string.'''


lista = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']

tamanhos = [len(s) for s in lista]
print(tamanhos) 