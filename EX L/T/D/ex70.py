'''Crie um dicion´ario que associa cada letra de uma palavra `a sua posi¸c˜ao.
'''
def posicoes_letras(palavra):
    dicionario_posicoes = {}
    for posicao, letra in enumerate(palavra):
        dicionario_posicoes[letra] = posicao
    return dicionario_posicoes
palavra_exemplo = 'python'
dicionario_resultado = posicoes_letras(palavra_exemplo)
print(dicionario_resultado)