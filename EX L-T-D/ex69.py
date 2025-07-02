'''Verifique se uma chave est´a presente em um dicion´ario e imprima seu valor, se
existir.
'''

def verificar_chave(dicionario, chave):
    if chave in dicionario:
        print(f"A chave '{chave}' está presente com o valor: {dicionario[chave]}")
    else:
        print(f"A chave '{chave}' não está presente.")

# Exemplo de uso
dicionario_exemplo = {'maçã': 10,'banana': 5,'laranja': 8}
chave_a_verificar = 'banana'
verificar_chave(dicionario_exemplo, chave_a_verificar)
chave_a_verificar = 'uva'
verificar_chave(dicionario_exemplo, chave_a_verificar)

