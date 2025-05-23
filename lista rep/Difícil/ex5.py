'''
Utilizando apenas laços de repetição, imprima um diamante formado por caracteres ASCII
sequenciais (começando em "A"), com altura ímpar informada pelo usuário.
Exemplo para altura 5:
A
ABA
ABCBA
ABA
A
'''

n = int(input("Digite um número ímpar para a altura do diamante: "))

for i in range(1, n + 1, 2):
    
    for espaco in range((n - i) // 2):
        print(" ", end="")
    
    for j in range(i // 2 + 1):
        print(chr(65 + j), end="")

    for j in range(i // 2 - 1, -1, -1):
        print(chr(65 + j), end="")

    print()

for i in range(n - 2, 0, -2):
    
    for espaco in range((n - i) // 2):
        print(" ", end="")
    
    for j in range(i // 2 + 1):
        print(chr(65 + j), end="")

    for j in range(i // 2 - 1, -1, -1):
        print(chr(65 + j), end="")

    print()

