'''Dada uma lista de nomes, retorne uma nova lista com os nomes em letras mai´usculas.'''

lista_nomes = ['sara', 'luiz', 'raiany', 'yasmin', 'luana']

lista_maiusculas = [nome.upper() for nome in lista_nomes]
print(lista_maiusculas)