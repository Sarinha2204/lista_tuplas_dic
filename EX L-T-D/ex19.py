''' Solicite nomes até que o usuário digite ”sair”. Armazene em uma lista e imprima.'''

nomes = []

while True:
    nome = input("Digite um nome(ou 'sair' para encerrar)")
    if nome.lower() == "sair":
        break
    
    nomes.append(nome)

print("Nomes digitados:", nomes)