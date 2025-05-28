''' Crie uma lista de palavras e remova as que tiverem menos de 4 letras.'''

lista_palavras = ['roxo', 'vermelho', 'preto', 'rosa', 'amarelo', 'azul']
palavras_filtradas = [palavra for palavra in lista_palavras if len(palavra) >= 4]
print(palavras_filtradas)