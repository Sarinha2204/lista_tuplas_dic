'''Dada uma lista de strings, ordene por ordem do n´umero de vogais em cada string'''

lista = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
def contar_vogais(s):
    return sum(1 for char in s.lower() if char in 'aeiou')
lista_ordenada = sorted(lista, key=contar_vogais)
print(lista_ordenada)