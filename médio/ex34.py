'''Faça um programa que leia números do usuário até digitar -1. Depois, imprima a
média.'''

numeros = []

while True:
    numero = int(input("Digite um número (-1 para sair): "))
    if numero == -1:
        break
    numeros.append(numero)