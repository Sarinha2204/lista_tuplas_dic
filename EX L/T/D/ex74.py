'''Dado um dicion´ario que associa nomes a listas de tarefas, imprima as tarefas de um
nome espec´ıfico.'''

def imprimir_tarefas(dicionario_tarefas, nome):
    if nome in dicionario_tarefas:
        tarefas = dicionario_tarefas[nome]
        if tarefas:
            print(f"Tarefas de {nome}: {', '.join(tarefas)}")
        else:
            print(f"{nome} não tem tarefas.")
    else:
        print(f"{nome} não encontrado no dicionário.")


dicionario_tarefas = {'Sara': ['Comprar pão', 'Estudar Python'],'Luiz': ['Lavar o carro', 'Fazer compras'],'Ray': []}

nome_a_procurar = 'Sara'
imprimir_tarefas(dicionario_tarefas, nome_a_procurar)
nome_a_procurar = 'Ray'
imprimir_tarefas(dicionario_tarefas, nome_a_procurar)
nome_a_procurar = 'Yas'
imprimir_tarefas(dicionario_tarefas, nome_a_procurar)
nome_a_procurar = 'Luiz'
imprimir_tarefas(dicionario_tarefas, nome_a_procurar)

