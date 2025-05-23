altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo(M para masculino e F para feminino): ")

if sexo == 'F':
    imc = (62.1 * altura) - 44,7
    print(f"Seu peso ideal é: {imc}")
elif sexo == 'M':
    imcM = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {imcM}")
else:
    print("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")
