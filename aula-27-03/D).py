import math
num1 = float(input("Informe um número: "))

if num1 <= 0:
    print("o numero informado é uma entrada irregular")
else:
    area = math.pi * (num1 **2)
    print(f"O valor da circunferência é: {area :.2f}")
