'''Fa¸ca uma fun¸c˜ao que receba um dicion´ario com tuplas como valores e retorne a
soma de todos os n´umeros nas tuplas.'''
def soma_tuplas(dicionario):
    total = 0
    for tupla in dicionario.values():
        total += sum(tupla)
    return total

dicionario_exemplo = {'a': (1, 2, 3),'b': (4, 5),'c': (6, 7, 8, 9)}
resultado = soma_tuplas(dicionario_exemplo)
print(f"A soma de todos os números nas tuplas é: {resultado}")