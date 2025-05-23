n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if (n1 > n2) and (n2 > n3):
    print(f"A ordem crescente é: {n1}, {n2}, {n3}")
elif (n2 > n1) and (n1 > n3):
    print(f"A ordem crescente é: {n2}, {n1}, {n3}")
elif (n2 > n3) and (n3 > n1):
    print(f"A ordem crescente é: {n2}, {n3}, {n1}")
elif (n3 > n1) and (n1 > n2):
    print(f"A ordem crescente é: {n3}, {n1}, {n2}")
elif (n3 > n2) and (n2 > n1):
    print(f"A ordem crescente é: {n3}, {n2}, {n1}")