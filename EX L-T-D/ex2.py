'''Solicite ao usu´ario 5 nomes e armazene em uma lista. Depois, imprima cada nome
em uma linha.'''

nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1} nome: ")
    nomes.append(nome)

print("Nomes digitados:")
for nome in nomes:
    print(nome)