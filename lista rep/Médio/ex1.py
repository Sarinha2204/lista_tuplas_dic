'''
Crie um programa usando laços que receba uma frase do usuário e 
retorne quantas vogais há nessa frase.
'''

frase = input("Digite uma frase: ")
vogais = "aeiou"
soma = 0

for letra in frase:
    if letra in vogais:
        soma += 1
print(f"A frase contém {soma} vogais.")