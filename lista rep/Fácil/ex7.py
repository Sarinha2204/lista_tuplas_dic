'''
Faça um programa que conte quantos divisores inteiros um número inteiro 
positivo possui utilizando laços.
'''

n = int(input("Digite um número: "))
soma = 0

for i in range(1, n + 1):
    if n % i == 0:
        soma += 1
print(f"O número {n} possui {soma} divisores inteiros positivos.")