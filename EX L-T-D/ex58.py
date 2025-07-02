'''Dada uma lista de n´umeros, encontre a subsequˆencia crescente mais longa.'''

def subsequencia_crescente(lista):
    if not lista:
        return []

    n = len(lista)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if lista[i] > lista[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_length = max(dp)
    index = dp.index(max_length)

    subsequencia = []
    while index != -1:
        subsequencia.append(lista[index])
        index = prev[index]

    return subsequencia[::-1]

lista_exemplo = [10, 22, 9, 33, 21, 50, 41, 60, 80]
resultado = subsequencia_crescente(lista_exemplo)
print(f"Lista original: {lista_exemplo}")