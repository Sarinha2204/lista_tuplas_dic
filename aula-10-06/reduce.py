'''MAP: aplica uma função a todos os itens de um iterável (como uma lista) e retorna 
um novo iterável com os resultados.

FILTER: filtra os itens de um iterável com base em uma função que retorna True ou 
False, retornando um novo iterável com os itens que passaram no teste.

REDUCE: aplica uma função cumulativa aos itens de um iterável, reduzindo-o a um único 
valor.


SINTAXE:
reduce(func, array)

'''

from functools import reduce
from random import randint


#numeros = []
#for i in range(10):
#    numeros.append(randint(1, 50))
#AO INVES DE USAR O DE CIMA USE O DE BAIXO
numeros = [randint(1, 50) for _ in range(10)]


soma = reduce(lambda x, y: x + y, numeros)
print(soma) 

maior = reduce(lambda x, y: x if x > y else y, numeros)

