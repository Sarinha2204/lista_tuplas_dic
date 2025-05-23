'''
Utilizando apenas laços de repetição, imprima uma pirâmide de 
números palíndromos com altura n.
Exemplo para n = 4:
   1
  121
 12321
1234321
'''

n = int(input("Digite um número: "))

for i in range(1, n + 1):
    for espaco in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()


