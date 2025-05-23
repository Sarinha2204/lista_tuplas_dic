'''
Crie um programa usando apenas laços que calcule o MDC (Máximo Divisor Comum)
entre dois números inteiros fornecidos pelo usuário.
Exemplo:
Entrada:
12
18
Saída:
6
'''

n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

menor = min(n1, n2)

for i in range(menor, 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        mdc = i
        break
print(f"O MDC entre {n1} e {n2} é: {mdc}")