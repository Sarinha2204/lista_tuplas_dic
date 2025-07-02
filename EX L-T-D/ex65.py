'''Fa¸ca um programa que recebe nomes de alunos e suas idades. Armazene usando
uma lista de tuplas e depois transforme em dicion´ario.'''

lista_alunos = []
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    idade = int(input(f"Digite a idade de {nome}: "))
    lista_alunos.append((nome, idade))

