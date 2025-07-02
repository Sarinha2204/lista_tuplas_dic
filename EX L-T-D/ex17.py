'''Crie uma lista com 5 números e calcule a média usando laço for'''

lista = [10, 20, 30, 40, 50]
soma = 0

for num in lista:
    soma += num
media = soma / len(lista)
print(f"A média dos números é: {media}")