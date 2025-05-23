A = int(input("Digite o valor 1: "))
B = int(input("Digite o valor 2: "))
C = int(input("Digite o valor 3: "))

delta = (B ** 2) * (4 * A * C)

if delta < 0:
    print("A conta não possui raízes reais.")
elif delta == 0:
    baskara = (-B + 1) / 2
    print(f"O resultado da equação de segundo grau com o delta igual a 0 é: {baskara}")
else:
    x1 = (-B + delta) / (2 * A)
    x2 = (-B - delta) / (2 * A)
    print(f"O resultado da equação de segundo grau é: {x1} , {x2}")