num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
num5 = int(input("Digite o quinto número: "))

soma_impares = 0
quantidade_impares = 0

if num1 % 2 != 0:
    soma_impares += num1
    quantidade_impares += 1
if num2 % 2 != 0:
    soma_impares += num2
    quantidade_impares += 1
if num3 % 2 != 0:
    soma_impares += num3
    quantidade_impares += 1
if num4 % 2 != 0:
    soma_impares += num4
    quantidade_impares += 1
if num5 % 2 != 0:
    soma_impares += num5
    quantidade_impares += 1


if quantidade_impares > 0:
    media_impares = soma_impares / quantidade_impares
    print(f"A média dos números ímpares é: {media_impares}")
else:
    print("Não há números ímpares para calcular a média.")
