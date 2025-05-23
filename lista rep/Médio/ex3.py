'''
Crie um programa que calcule o valor da seguinte série até o 
n-ésimo termo informado pelo usuário, usando apenas laços:
S=1/1+2/3+3/5+4/7+⋯+n/2n−1
'''

n = int(input("Digite um número: "))
soma = 0

for i in range(1, n+ 1):
    termo = i /(2 * i - 1)
    soma += termo
print(f"O valor da série até o {n}-ésimo termo é: {soma}")