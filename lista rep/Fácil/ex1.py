'''Faça um programa usando laços que some todos os números inteiros de 1 até n
fornecido pelo usuário.
'''
n = int(input("Digite um número:"))
soma= 0

for i in range(int(n) +1):
    soma += i
print(f"O resultado é: {soma}")