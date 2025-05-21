'''Simule uma pilha usando append e pop. Mostre a pilha a cada operação.'''


def simulador_pilha():
    pilha = []


    pilha.append(1)
    print(f"Pilha após adicionar: {pilha}")
    
    pilha.append(2)
    print(f"Pilha após adicionar: {pilha}")
    
    pilha.append(3)
    print(f"Pilha após adicionar: {pilha}")
    
    pilha.append(4)
    print(f"Pilha após adicionar: {pilha}")
    
    pilha.pop()
    print("Pilha após remover:", pilha)
    
    pilha.pop()
    print("Pilha após remover:", pilha)
    
    pilha.pop()
    print("Pilha após remover:", pilha)
    
simulador_pilha()
