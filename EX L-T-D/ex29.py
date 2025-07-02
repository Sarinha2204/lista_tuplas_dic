'''Crie um menu interativo que permita adicionar, remover, listar ou sair de um 
programa que manipula listas.'''

lista = []

while True:
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Listar")
    print("4 - Sair")
    
    op = input("Opção: ")

    if op == "1":
        item = input("Item: ")
        lista.append(item)

    elif op == "2":
        item = input("Item: ")
        if item in lista:
            lista.remove(item)
        else:
            print("Não encontrado.")

    elif op == "3":
        print(lista)

    elif op == "4":
        break

    else:
        print("Opção inválida.")
