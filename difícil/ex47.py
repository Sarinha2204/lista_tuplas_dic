'''Solicite notas de alunos e armazene como tuplas (nome, nota). Ordene a lista pela
nota em ordem decrescente.'''

lista_notas = []
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    try:
        nota = float(input(f"Digite a nota de {nome}: "))
        lista_notas.append((nome, nota))
    except ValueError:
        print("Nota inválida. Por favor, insira um número.")
        
lista_notas.sort(key=lambda x: x[1], reverse=True)
for aluno, nota in lista_notas:
    print(f"{aluno}: {nota:.2f}")