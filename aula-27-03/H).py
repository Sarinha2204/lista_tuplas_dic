num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))

if (num1 > num2) and (num1 > num3):
    print(f"O maior número é: {num1}")
elif (num2 > num1) and (num2 > num3):
    print(f"O maior número é: {num2}")
elif (num3 > num1) and (num3 > num2):
    print(f"O maior número é: {num3}")