'''Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a
ordem.'''

lista = ['Sara', 'Sara', 'Luiz', 'Luana','Luiz', 'Luana']

resultado = []
vistos = set()

for nome in lista:
    if nome not in vistos:
        resultado.append(nome)
        vistos.add(nome)

print(resultado)