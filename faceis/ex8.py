'''Dada a lista cores = ["azul", "verde", "amarelo"], insira a cor "vermelho"
na posição 1.'''


lista = ["azul", "verde", "amarelo"]

lista.insert(0, 'vermelho')

for i in range(len(lista)):
    print(lista[i])
