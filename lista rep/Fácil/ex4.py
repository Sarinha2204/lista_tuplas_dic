'''
Crie um programa que imprima todos os números pares até o número fornecido pelo
usuário usando laços.
'''

n = int(input("digite um número: "))

for i in range(n + 1):
    if i % 2 == 0:
        print(i)
