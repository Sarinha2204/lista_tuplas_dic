'''Construa um sistema de invent´ario onde cada item ´e mapeado para uma tupla com
quantidade e pre¸co.'''

def sistema_inventario():
    inventario = {}

    while True:
        item = input("Digite o nome do item (ou 'sair' para encerrar): ")
        if item.lower() == 'sair':
            break

        quantidade = int(input(f"Digite a quantidade de {item}: "))
        preco = float(input(f"Digite o pre¸co unit´ario de {item}: "))

        inventario[item] = (quantidade, preco)

    return inventario

inventario_resultado = sistema_inventario()
print("Inventário:")