'''Dado um dicion´ario de alunos (chave = nome, valor = tupla de notas), imprima
apenas os aprovados (m´edia >= 7).'''

def alunos_aprovados(dicionario_alunos):
    for aluno, notas in dicionario_alunos.items():
        media = sum(notas) / len(notas)
        if media >= 7:
            print(f"{aluno} está aprovado com média {media:.2f}")

# Exemplo de uso
dicionario_alunos = {'Sara': (8, 7, 9),'Luiz': (6, 5, 7),'Ray': (9, 10, 8),'Yas': (5, 6, 4)}   
alunos_aprovados(dicionario_alunos)
