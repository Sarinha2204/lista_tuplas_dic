'''Implemente um sistema que simule um carrinho de compras: adi¸c˜ao, remo¸c˜ao e
total de itens com pre¸cos.
class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"
class Carrinho:
    '''