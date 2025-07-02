'''Crie uma lista de dicion´arios com nome, idade e cidade. Imprima os dados de cada
pessoa.'''
lista_pessoas = [
    {'nome': 'Sara', 'idade': 18, 'cidade': 'São Paulo'},
    {'nome': 'Raiany', 'idade': 17, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Yasmin', 'idade': 22, 'cidade': 'Belo Horizonte'},
    {'nome': 'Luiz', 'idade': 20, 'cidade': 'Curitiba'},
    {'nome': 'Luiza', 'idade': 19, 'cidade': 'Porto Alegre'}
]
for pessoa in lista_pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
