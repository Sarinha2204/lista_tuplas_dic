'''
Faça um programa que exiba a tabuada de multiplicação do número 
fornecido pelo usuário (de 1 a 10)
'''
n = int(input("Digite um número:"))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
