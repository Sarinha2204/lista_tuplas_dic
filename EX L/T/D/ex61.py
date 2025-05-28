'''Crie um dicion´ario onde as chaves s˜ao nomes de pessoas e os valores s˜ao listas com
trˆes notas. Calcule a m´edia de cada aluno.
'''

notas_alunos = {'Sara': [7.5, 8.0, 9.0],'Luiz': [6.0, 7.5, 8.5],'Luana': [9.0, 9.5, 10.0],'Raiany': [5.0, 6.5, 7.0]}   
medias = {nome: sum(notas) / len(notas) for nome, notas in notas_alunos.items()}
print("Médias dos alunos:")
for aluno, media in medias.items():
    print(f"{aluno}: {media:.2f}")
