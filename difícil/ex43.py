'''Implemente um sistema que simule um carrinho de compras: adi¸c˜ao, remo¸c˜ao e
total de itens com pre¸cos.'''

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"
class Carrinho:
    def __init__(self):
        self.itens = []
    
    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"Item '{item.nome}' adicionado ao carrinho.")
    
    def remover_item(self, nome_item):
        for item in self.itens:
            if item.nome == nome_item:
                self.itens.remove(item)
                print(f"Item '{nome_item}' removido do carrinho.")
                return
        print(f"Item '{nome_item}' não encontrado no carrinho.")
    
    def total(self):
        total = sum(item.preco for item in self.itens)
        return total
    
    def listar_itens(self):
        if not self.itens:
            print("O carrinho está vazio.")
        else:
            print("Itens no carrinho:")
            for item in self.itens:
                print(item)

carrinho = Carrinho()
item1 = Item("Camiseta", 49.90)
item2 = Item("Calça Jeans", 89.90)
item3 = Item("Tênis", 199.90)
carrinho.adicionar_item(item1)
carrinho.adicionar_item(item2)
carrinho.adicionar_item(item3)
carrinho.listar_itens()
print(f"Total do carrinho: R${carrinho.total():.2f}")
carrinho.remover_item("Calça Jeans")
carrinho.listar_itens()
print(f"Total do carrinho após remoção: R${carrinho.total():.2f}")
carrinho.remover_item("Blusa")
carrinho.listar_itens()
print(f"Total do carrinho após tentativa de remoção: R${carrinho.total():.2f}")
