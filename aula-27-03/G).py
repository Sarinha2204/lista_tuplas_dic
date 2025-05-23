nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))
nota3 = float(input("Digite a nota do terceiro bimestre: "))
nota4 = float(input("Digite a nota do quarto bimestre: "))

if (nota1 < 0) or (nota2 < 0) or (nota3 < 0) or (nota4 < 0):
    print ("As notas não podem ser menores que 0.")
else:
    soma = nota1 + nota2 + nota3 + nota4
    media = soma / 4
if media >= 6:
    print ("O aluno esta aprovado")
else:
    print("O aluno esta reprovado.")