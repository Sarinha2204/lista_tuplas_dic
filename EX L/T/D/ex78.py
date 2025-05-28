'''Transforme uma lista de palavras em um dicion´ario que agrupe as palavras por
tamanho.'''

def agrupar_por_tamanho(palavras):
    dicionario_tamanho = {}
    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho not in dicionario_tamanho:
            dicionario_tamanho[tamanho] = []
        dicionario_tamanho[tamanho].append(palavra)
    return dicionario_tamanho
lista_palavras = ['roxo', 'vermelho', 'preto', 'rosa', 'amarelo', 'azul']
dicionario_resultado = agrupar_por_tamanho(lista_palavras)
print(f"Dicionário agrupado por tamanho: {dicionario_resultado}")