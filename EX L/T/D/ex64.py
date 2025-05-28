'''Crie um dicion´ario que mapeia n´umeros de 1 a 5 para seus quadrados, usando la¸co
for.'''

dicionario_quadrados = {}
for i in range(1, 6):
    dicionario_quadrados[i] = i ** 2
print(dicionario_quadrados)