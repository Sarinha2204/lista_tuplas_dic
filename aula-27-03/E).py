nome = input("informe o nome do funcionário: ")
quantidade_de_funcoes = float(input("informe a quantidade de funções: "))
valor_das_funcoes = float(input("informe o valor das funções: "))

if (quantidade_de_funcoes <= 0) and (valor_das_funcoes <= 0):
    print("O valor informado é inválido")
else: 
    salario_bruto = quantidade_de_funcoes * valor_das_funcoes
    desconto = salario_bruto * 0.08
    salario_liquido = salario_bruto - desconto
    
    print(f"o nome do programador é: {nome}")
    print(f"o valor do salário bruto é: {salario_bruto}")
    print(f"o valor do salário líquido: {salario_liquido}")