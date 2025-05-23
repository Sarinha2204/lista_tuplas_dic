'''
Faça um programa que imprima a seguinte série incremental, com base num valor n:
Exemplo:
Entrada: 5
Saída:
1
12
123
1234
12345
'''

n = int(input("Digite um número: "))

for i in range(1, n + 1):
    linha = ""
    for j in range(1, i + 1):
        print(j, end="")
    print()

