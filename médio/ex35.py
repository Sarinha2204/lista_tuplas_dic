'''Crie uma lista de tuplas contendo nomes e idades. Imprima os nomes das pessoas
com mais de 18 anos.
'''

lista_pessoas = [('Sara', 18), ('Raiany', 17), ('Yasmin', 22), ('Luiz', 20), ('Luiza', 19)]

maiores_de_idade = [nome for nome, idade in lista_pessoas if idade > 18]
print(maiores_de_idade)