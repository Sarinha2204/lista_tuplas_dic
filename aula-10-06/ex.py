from functools import reduce
from random import randint


numeros = [randint(1, 10) for _ in range(10)]
soma = reduce(lambda x, y: x + y, numeros)
print(soma) 
# maior = reduce(lambda x, y: x if x > y else y, numeros)#encontrar o maior 


#EX.1 Calcular a media dos quadrados dos numeros pares de uma lista

media = reduce(lambda x, y: x + y, 
               map(lambda x: x ** 2, 
                   filter(lambda x: x % 2 == 0, numeros))) / len(list(filter(lambda x: x % 2 == 0, numeros)))

#EX.2 Encontrar o maior numero impar apos elevar ao cubo

maior = reduce(lambda x, y: x if x > y else y, 
               filter(lambda x: x % 2 != 0, 
                      map(lambda x: x ** 3, numeros)))
print(maior)


#EX.3 Somar os quadrados dos números que são multiplos de 3

soma = reduce(lambda x, y: x+y, 
              map(lambda x: x**2, 
                  filter(lambda x: x % 3==0, numeros)))
print(soma)


#EX.4 *REDUCE Calcular o produto* dos *FILTER números pares* após *MAP multiplicar por 2*

produto = reduce(lambda x,y: x*y,
                 map(lambda x: x * 2, 
                     filter(lambda x: x % 2 == 0, numeros)))

#EX.5 *REDUCE Encontrar a média dos números* *REDUCE que são maiores que 5* após *MAP elevar ao quadrado*

media_maiores_5 = reduce(lambda x, y: x+y, 
                         filter(lambda x, y: x > 5, 
                                map(lambda x: x**2, numeros))) / len(list(filter(lambda x: x > 5, numeros)))


#EX.6 Calcular a soma dos cubos dos numeros que são menores que a média da lista

media_lista = reduce(lambda x,y: x+y, 
                     map(lambda x: x**3, 
                         filter(lambda x: x < reduce(lambda x,y: x+y, numeros) / len((numeros))), numeros))