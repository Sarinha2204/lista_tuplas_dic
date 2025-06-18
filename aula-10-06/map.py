'''MAP: aplica uma função a todos os itens de um iterável (como uma lista) e retorna 
um novo iterável com os resultados.


Sintaxe:
map(func, iterable)
filter(func, iterable)
reduce(func, iterable)
'''

#Dobrar todos os números de uma lista
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)

#Converter lista de strings para inteiros
str_numeros = ['1', '2', '3', '4']
inteiros = list(map(int, str_numeros))
print(inteiros)

#Converter todas as letras de uma string para maiúsculas
palavras = ['python', 'map', 'função']
maiusculas = list(map(str.upper, palavras))
print(maiusculas)  # Saída: ['PYTHON', 'MAP', 'FUNÇÃO']

