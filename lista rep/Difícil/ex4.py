'''
Receba um número inteiro n maior que 1 e, utilizando apenas laços de repetição, apresente
sua fatoração em números primos.
'''

n = int(input("Digite um número inteiro maior que 1: "))

fator = 2
primeira = True

while n > 1:
    if n % fator == 0:
        if not primeira:
            print("x", end=" ")
        print(fator, end=" ")
        n = n // fator
        primeira = False
    else:
        fator += 1
