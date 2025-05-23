'''
Imprima todos os pares de números primos gêmeos até um limite n utilizando
exclusivamente laços de repetição. Números primos gêmeos são primos cuja diferença é
exatamente 2.
Exemplo para n = 20:
(3, 5), (5, 7), (11, 13), (17, 19)
'''

n = int(input("Digite um número: "))

def eh_primo(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(2, n - 1):
    if eh_primo(i) and eh_primo(i + 2):
        print(f"({i}, {i  + 2})")