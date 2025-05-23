#import random
'''
LISTA / TUPLAS / DIC.

Lista -> coleções heterogênas de objetos, podem ser qualquer tipo, inclusive outras listas

-> são mutáveis

exemplo: [0, 1, 10, "beto", [0.2, 0.3]]

n1, n2, n3, n4 = 1, 2, 3, 4

lista-01 = [1, 2, 3, 4, 5, 6]

lista-02 = [3.14, 'beto, True, []]

'''

lista = [1, 2, 3]
print(lista)


nome = "beto"
#len -> função que retorna o tamanho de uma coleção
print(len(nome))


progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP', 'Metalica', 'U2']
progs[3]  = 'Metalica'
progs[5]  = 10

#PRIMEIRA FORMA
for i in range(len(progs)):
    print(progs[i])


#SEGUNDA FORMA
for prog in progs:
    print(prog)

#incluir novo elemento
progs.append('Guns')

#forma mais simples de adicionar um elemento(-1 = ultimo, -2 = penultimo...)
progs[-1] = 'Novo'

#ordenar
progs.sort()

#inverter a lista
progs.reverse

''' PESQUISAR:
zip
pop
remove
set
frozenset
'''
for i, p in enumerate(progs):
    print(f"Posição {i} e elemento = {p}")


#dada as seguintes listas [A, B C] e [D, E, F] como poderiamos juntar?

lista1 = ['A', 'B', 'C']
lista2 = ['D', 'E', 'F']

listas = lista1 + lista2
print(listas)



'''pensando em listas de 50 alunos onde serao lidas (random) 4 notas (0 - 100)
mostre:
    a % de alunos aprovados
    a % de alunos reprovados

    imprima os 5 primeiros alunos com media mais alta
    imprima os 5 piores alunos
    imprima a nota mais alta, a posicao e qual aluno pertence

#import random(ta la em cima)

notas= []

for i in range(1, 51):
    nota = random.randint(0, 100)
    notas.append((f'Aluno {i}', nota))
    
for aluno, nota in notas:
    print(f"{aluno} : {nota}")
'''


# Tuplas -> semelhantes as listas, porém não são mutáveis: não acrescenta, nao apaga, não faz 
# atribuições

tupla = (1, 2, 3, 4)

t1 = (1,)

print(tupla[0])

for t in tupla:
    print(t)

lista = list(tupla)

lista_tupla = ([1,2,3], [2,3], ('beto', 'vitor', 'rafael'))


#união, interseção e diferença