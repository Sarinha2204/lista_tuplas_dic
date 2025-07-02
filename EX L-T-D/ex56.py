'''Crie uma lista de listas representando uma matriz 3x3 e some os valores de cada
linha.'''
matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

soma_linhas = [sum(linha) for linha in matriz]
print(f"Matriz: {matriz}")