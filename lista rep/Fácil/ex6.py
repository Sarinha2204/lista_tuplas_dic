'''
Faça um programa que calcule o fatorial de um número inteiro positivo usando apenas
laços.
'''

n = int(input("Digite um número inteiro e positivo: "))
fatorial = 1

while n > 1:
    fatorial = fatorial * n
    n = n - 1
print("O fatorial do numero inteiro é {}" .format(fatorial))