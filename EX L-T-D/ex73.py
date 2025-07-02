'''Crie uma fun¸c˜ao que inverta as chaves e valores de um dicion´ario'''

def inverte_dicionario(dicionario):
    dicionario_invertido = {}
    for chave, valor in dicionario.items():
        if valor not in dicionario_invertido:  
            dicionario_invertido[valor] = chave
        else:
            print(f"Valor {valor} já existe como chave no dicionário invertido.")
    return dicionario_invertido


dicionario_exemplo = {'maçã': 10, 'banana': 5, 'laranja': 8}
dicionario_invertido = inverte_dicionario(dicionario_exemplo)
print(dicionario_invertido)