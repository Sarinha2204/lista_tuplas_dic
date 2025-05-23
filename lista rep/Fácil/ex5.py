'''
Faça um programa que some apenas os números ímpares até um número inteiro positivo
informado pelo usuário usando laços.
'''
n = int(input("Digite um número(inteiro e positivo): "))
soma = 0

for i in range(n + 1):
    if i % 2 == 1:
        soma += i
print(soma)