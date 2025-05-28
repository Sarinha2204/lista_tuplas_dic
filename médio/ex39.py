'''Faça a união de duas listas sem usar o operador +.'''

lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

lista_unida = lista1.copy()
for item in lista2:
    lista_unida.append(item)