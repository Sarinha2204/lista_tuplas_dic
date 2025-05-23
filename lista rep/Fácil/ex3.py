'''
Crie um programa que faça uma contagem regressiva, do número fornecido até 0, utilizando
laços de repetição.
'''

n = int(input("Digite um número: "))

for i in range(n, 0, -1):
    print(i)