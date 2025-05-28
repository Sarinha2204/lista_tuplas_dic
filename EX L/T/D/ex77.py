'''Crie um dicion´ario onde as chaves s˜ao c´odigos de produtos e os valores s˜ao tuplas
(nome, pre¸co).'''

def criar_dicionario_produtos():
    dicionario_produtos = {'001': ('Maçã', 1.20),'002': ('Banana', 0.80),'003': ('Laranja', 1.00),'004': ('Uva', 2.50),'005': ('Pera', 1.50)}
    return dicionario_produtos

dicionario_produtos = criar_dicionario_produtos()
for codigo, (nome, preco) in dicionario_produtos.items():
    print(f"Código: {codigo}, Produto: {nome}, Preço: R${preco:.2f}")
