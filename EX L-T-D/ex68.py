'''Converta uma lista de tuplas (chave, valor) em um dicion´ario.
'''

def lista_para_dicionario(lista_tuplas):
    dicionario = {}
    for chave, valor in lista_tuplas:
        dicionario[chave] = valor
    return dicionario

lista_exemplo = [('maçã', 10), ('banana', 5), ('laranja', 8)]   
dicionario_resultado = lista_para_dicionario(lista_exemplo)
print(dicionario_resultado)