num1 = int(input("Digite um número:"))
num2 = int (input("Digite outro número:"))

if (num1 <= 0) or (num2 <= 0):
    print ("Números inválidos")
else:
        AUX = num1
        num1 = num2
        num2 = AUX
        print(f"Após a troca: num1 = {num1} e num2 = {num2}")