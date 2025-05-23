from random import randint

'''
Dicionários:

Cada chave é única dentro do dicionário.
Os valores podem ser de qualquer tipo.
Dicionários são mutáveis: você pode adicionar, remover ou alterar itens.

sintaxe: 
dicionario = {'a':( 1, 2 [1, 21 {1:20, 2:30}]), 'b' : 2, 'c': 3,}*obrigatório uso de chaves*

'''

#dic = {'nome1':'sara', 'nome2':'Raiany', 'nome3':'Yasmin'}

#dic['nota'] = 10

#usa-se o print para debugar o código
#print(dic)

# dic =  {(1, 2), (3, 4): 5}
# pode usar tupla dentro do dicionário, pois a tupla é imutável
'''
items = dic.items()
chaves = dic.keys()
valores = dic.values()

print(f'Itens = {items}')
print(f'Chaves = {chaves}')
print(f'Valores = {valores}')
'''
# get

'''
Imprimindo todas as chaves e valores do dicionário
for i, j in dic.items():
    print(f'Chave: {i} - Valor: {j}')

#Imprimindo apenas as chaves
for i in dic.items():
    print(f'Chave: {i}')
    
Imprimindo apenas os valores
for j in dic.items():
    print(f'Valor: {j}')'''
    

'''EX 1
Leie o nome de 5 pessoas e armazene em um dicionario

dic = {}


for i in range(5):
    nome = input('Digite o nome: ')
    dic [i] = nome
    
print(dic)'''

'''EX 2
crie um programa para gerar um dicionario com 20 número inteiros,
mostre as soma de todos os elementos

dic = {}
soma = 0

for i in range(20):
    num = randint(1, 20)
    dic[i] = num
for i in dic:
    soma += dic[i]

#pode fazer a soma assim também
#soma = sum(dic.values())


print(f'Os elementos são: {dic}')
print(f'A soma dos 20 elementos é: {soma}')'''

#Compreensão de listas
lista = [i for i in range(5)] # -> [0, 1, 2, 3, 4]
print(lista)

for i in [0.2, 0.4, 0.6, 0.8]:
    pass

#COMO TRABALHAR COM COMPREENSÃO DE LISTAS

#lista2 = [x,y for x in range(5) for y in range(5) if x != y: x+=2]

'''EX 3
Crie un programa para ler o nome, a matricula e as 4 notas de 5 alunos e armazene em um dicionario
= {matricula:nome, notas:[n1, n2, n3, n4]}
as notas podem ser geradas de formas aleatorias com o uso de compreensao de listas

a) mostrar o aluno com a maior media
b) a % de aluno com a media maior que 8
c) a % de alunos que estariam reprovados, considerando a media < 4
'''

for i in range(5):
    nome = input("Digite o nome do aluno:")
    matricula = input('Digite a  matrícula do aluno:')
    notas = [randint(0,10)for i in range(4)]
    media = sum(notas)/4
    

