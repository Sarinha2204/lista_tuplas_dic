n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

soma_pares = 0

if n1 % 2 == 0:
    soma_pares += n1

if n2 % 2 == 0:
    soma_pares += n2

if n3 % 2 == 0:
    soma_pares += n3

if n4 % 2 == 0:
    soma_pares += n4

    print(f"A soma dos número pares é: {soma_pares}")