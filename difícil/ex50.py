'''Crie uma lista de tuplas com nomes e idades e retorne a pessoa mais velha e a mais
nova.'''

lista_pessoas = [('Sara', 18), ('Raiany', 17), ('Yasmin', 22), ('Luiz', 20), ('Luiza', 19)]
def pessoa_extrema(lista, tipo='mais_velha'):
    if not lista:
        return None
    
    if tipo == 'mais_velha':
        return max(lista, key=lambda x: x[1])
    elif tipo == 'mais_nova':
        return min(lista, key=lambda x: x[1])
    else:
        raise ValueError("Tipo deve ser 'mais_velha' ou 'mais_nova'.")
mais_velha = pessoa_extrema(lista_pessoas, 'mais_velha')
mais_nova = pessoa_extrema(lista_pessoas, 'mais_nova')