'''Implemente um sistema que funcione como fila de banco, com chegada e atendimento
dos clientes.
'''

class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome
class FilaBanco:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, cliente):
        self.fila.append(cliente)
        print(f"Cliente {cliente} adicionado à fila.")

    def atender_cliente(self):
        if self.fila:
            cliente_atendido = self.fila.pop(0)
            print(f"Atendendo cliente: {cliente_atendido}")
        else:
            print("Nenhum cliente na fila.")

    def mostrar_fila(self):
        if self.fila:
            print("Clientes na fila:")
            for cliente in self.fila:
                print(cliente)
        else:
            print("A fila está vazia.")

fila_banco = FilaBanco()
fila_banco.adicionar_cliente(Cliente("Alice"))