'''Solicite ao usu´ario que digite pares (produto, pre¸co) e armazene em um dicion´ario.
Permita pesquisar o pre¸co por produto.'''

def adicionar_produto(produtos):
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos[produto] = preco
    print(f"Produto '{produto}' adicionado com sucesso!")
    
def pesquisar_preco(produtos):
    produto = input("Digite o nome do produto para pesquisar o preço: ")
    if produto in produtos:
        print(f"O preço do produto '{produto}' é R${produtos[produto]:.2f}")
    else:
        print(f"Produto '{produto}' não encontrado.")
def main():
    produtos = {}
    
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Pesquisar preço por produto")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_produto(produtos)
        elif opcao == '2':
            pesquisar_preco(produtos)
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()
