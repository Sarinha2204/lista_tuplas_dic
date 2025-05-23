'''
Faça um programa que, utilizando laços, imprima o seguinte padrão numérico invertido
baseado no número inteiro informado pelo usuário.
Exemplo:
Entrada:
5
Saída:
12345
1234
123
12
1
'''

n = int(input("Digite um número: "))

for i in range(n, 0, -1):
    linha = ""
    for j in range (1, i + 1):
        print(j, end="")
    print()