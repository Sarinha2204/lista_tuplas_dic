'''
Dado um valor inteiro positivo n, imprima os primeiros n termos da sequência de Fibonacci
em ordem decrescente utilizando apenas laços de repetição.
Exemplo para n = 6:
5 3 2 1 1 0
'''

n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

fibonacci = []
a,b = 0, 1

for i in range(n):
    fibonacci.append(a)
    a,b = b, a + b

for i in range(n -1, -1, -1):
    print(fibonacci[i], end="")