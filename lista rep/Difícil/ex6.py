'''
Utilizando apenas laços de repetição, calcule a soma dos primeiros n termos da série
harmônica alternada:
* Uma série harmônica é uma série infinita em matemática, formada pela soma dos inversos
dos números naturais consecutivos
'''

n = int(input("Digite a quantidade de termos da série: "))

soma = 0.0

for i in range(1, n + 1):
    if i % 2 == 0:
        soma -= 1 / i
    else:
        soma += 1 / i

print(f"A soma dos {n} primeiros termos da série harmônica alternada é: {soma}")
