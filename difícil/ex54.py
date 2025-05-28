'''Crie uma fun¸c˜ao que agrupe palavras por tamanho em um dicion´ario'''

def agrupar_por_tamanho(palavras):
    dicionario = {}
    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho not in dicionario:
            dicionario[tamanho] = []
        dicionario[tamanho].append(palavra)
    return dicionario

palavras_exemplo = ['roxo', 'vermelho', 'preto', 'rosa', 'amarelo', 'azul'] 
resultado = agrupar_por_tamanho(palavras_exemplo)
print("Dicionário agrupado por tamanho:", resultado)