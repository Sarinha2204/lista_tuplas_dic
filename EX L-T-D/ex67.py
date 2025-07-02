'''Crie um sistema de agenda onde cada contato ´e uma chave e o valor ´e uma lista de
telefones.'''

agenda = {}
def adicionar_contato(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        agenda[nome] = [telefone]

def exibir_agenda():
    for contato, telefones in agenda.items():
        print(f"{contato}: {', '.join(telefones)}")

def main():
    while True:
        nome = input("Digite o nome do contato (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        telefone = input(f"Digite o telefone de {nome}: ")
        adicionar_contato(nome, telefone)
    
    print("\nAgenda de Contatos:")
    exibir_agenda()
if __name__ == "__main__":
    main()