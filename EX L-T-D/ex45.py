'''. Faça uma função que receba uma lista de listas e retorne uma lista ”achatada”
(flatten)'''

def achatar_lista(lista_de_listas):
    lista_flat = []
    for sublista in lista_de_listas:
        for item in sublista:
            lista_flat.append(item)
    return lista_flat

lista_de_listas = [[1, 2, 3], [4, 5], [6, 7, 8]]    
print(achatar_lista(lista_de_listas))