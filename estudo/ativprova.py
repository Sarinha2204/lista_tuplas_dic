from functools import reduce
'''
Um sistema de segurança utiliza uma escada codificada onde o nível de acesso depende da soma dos degraus recursivamente.

Implemente uma função recursiva soma_degraus(n) que retorna a soma de todos os degraus de n até 0. O sistema deve solicitar ao usuário um número inteiro positivo n, calcular o total da soma dos degraus e exibir:

Soma total dos degraus: X
Exemplo:
Se o usuário digitar 4, a função deverá realizar: 4 + 3 + 2 + 1 + 0 = 10.

Restrição:
Não é permitido usar sum() nem estruturas de repetição (for ou while).


def soma_degraus(n):
    if n <= 0 :
        return 0
    return n + soma_degraus(n - 1)

n = int(input("Digite um número inteiro positivo: "))
print(f"Soma total dos degraus: {soma_degraus(n)}")'''



'''
Você está desenvolvendo um programa para um centro de inteligência. 
Seu objetivo é filtrar apenas os números "confiáveis" de uma lista de dados. 
Um número é considerado confiável se for divisível por 5 e par ao mesmo tempo.

Solicite ao usuário 10 números inteiros, um por um.

Crie uma função confiavel(n) que retorna True se o número for divisível por 5 e par, 
caso contrário False.

Use a função filter() com a função confiavel para filtrar os números.

Exiba a quantidade de números confiáveis e a lista resultante.


def confiavel(n):
    confiavel = filter(lambda n: n % 5 == 0 and n % 2 == 0, [n])
    return len(list(confiavel)) > 0
numeros_confiaveis = 0
for i in range(10):
    n = int(input("Digite um número inteiro:"))
    if confiavel(n):
        numeros_confiaveis += 1
print(f"Quantidade de Números confiáveis: {numeros_confiaveis}")
'''



'''Você desenvolveu uma máquina que transforma números utilizando operações de dobro e 
soma final.
Solicite ao usuário 6 números inteiros.
Use a função map() com uma função lambda para dobrar cada número.
Use reduce() para somar todos os valores transformados.
Exiba a lista original, a lista dobrada e o valor final da soma.
Exemplo de saída:

Entrada: [1, 2, 3, 4, 5, 6]
Dobrados: [2, 4, 6, 8, 10, 12]
Soma total: 42
Dica: Importe reduce do módulo functools.

lista = [int(input("Digite um número inteiro: ")) for _ in range(6)]

numeros_dobrados = list(map(lambda x: x *2, lista))
soma_total = reduce(lambda x, y: x + y, numeros_dobrados)

print(f"Entradas: {lista}")
print(f"Dobrados: {numeros_dobrados}")
print(f"Soma total: {soma_total}")'''

'''
Um laboratório desenvolveu um codificador que calcula uma sequência numérica 
chamada Fractal Temporal, seguindo a seguinte lógica:
Dado um número inteiro positivo n, o resultado do Fractal é:
Se n == 0, o resultado é 1
Se n é ímpar, o resultado é n * fractal(n - 1)
Se n é par, o resultado é fractal(n // 2) + fractal(n - 1)

Tarefa:
Implemente a função fractal(n) recursivamente e, a partir da entrada do usuário (n), 
exiba o resultado com a seguinte saída:

Resultado do Fractal Temporal para N = X: Y

#fractal = [int(input("Digite um número inteiro"))]

def fractal(n):
    if n == 0:
        return 1
    elif n % 2 != 0: 
        return n * fractal(n - 1)
    else: 
        return  fractal(n // 2) + fractal(n - 1)

n = int(input("Digite um número inteiro: "))
print(f"Resultado do Fractal Temporal para N = {n}: {fractal(n)}")'''


'''
Você está desenvolvendo um redutor lógico que analisa a paridade de uma sequência e 
produz um índice de segurança. A lógica é a seguinte:
Solicite ao usuário 8 números inteiros.
Use map() com uma função lambda para converter:
Números pares → 2
Números ímpares → -1
Use reduce() para somar todos os valores da lista convertida.

Se o total for:
Maior que 0 → exibir "Segurança Estável"
Igual a 0 → exibir "Zona Neutra"
Menor que 0 → exibir "Paridade Crítica! Alerta vermelho"

Exemplo:
Entrada: [2, 4, 6, 3, 5, 7, 9, 10]
Convertido: [2, 2, 2, -1, -1, -1, -1, 2]
Soma: 4

Saída:
Índice de Segurança: 4
Segurança Estável



n = [int(input("Digite um número inteiro: ")) for i in range(8)]

seguranca = map(lambda x: 2 if x % 2 == 0 else -1, n)
soma = reduce(lambda x, y: x + y, seguranca)

if soma > 0:
    print("Segurança Estável")
elif soma == 0:
    print("Zona Neutra")
else:
    print("Paridade Crítica! Alerta vermelho")

print(f"Índice de Segurança: {soma}")'''







'''Filtragem Inicial (kwargs):
Se ignorar_negativos=True, descarte os negativos de *args.
Transformação (map):
Para cada número:
Par → n // 2
Ímpar → n * 3 + 1 (Collatz)
Filtragem (filter):
Mantenha apenas:
Números primos
Maiores que limite_primo
Redução (reduce):
Calcule a soma de todos os valores filtrados
Análise Recursiva:
Crie uma função recursiva maior_seq_primos(lista, atual=0, maior=0) que determina o 
tamanho da maior sequência consecutiva de primos na lista filtrada.
✅ Saída esperada:
O sistema imprime:

Pacotes recebidos: [lista original]
Transformados: [...]
Filtrados (primos > limite): [...]
Soma final: X
Maior sequencia consecutiva de primos: Y

Status do Núcleo:
- ESTÁVEL, se Y >= 3 e soma >= estabilidade_min
- INSTÁVEL, se Y < 3
- COLAPSANDO, se soma < colapso_min'''


def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def maior_seq_primos(lista, atual=0, maior=0):
    if not lista:
        return maior
    if primo(lista[0]):
        return maior_seq_primos(lista[1:], atual + 1, max(maior, atual + 1))
    else:
        return maior_seq_primos(lista[1:], 0, maior)

def processar_dados(*args, **kwargs):
    ignorar_negativos = kwargs.get("ignorar_negativos", True)
    limite_primo = kwargs.get("limite_primo", 10)
    colapso_min = kwargs.get("colapso_min", 20)
    estabilidade_min = kwargs.get("estabilidade_min", 50)
    dados = [n for n in args if not ignorar_negativos or n >= 0]
    transformados = list(map(lambda n: n // 2 if n % 2 == 0 else n * 3 + 1, dados))
    filtrados = list(filter(lambda n: primo(n) and n > limite_primo, transformados))
    soma_total = reduce(lambda x, y: x + y, filtrados, 0)
    seq_max = maior_seq_primos(filtrados)
    
    if seq_max >= 3 and soma_total >= estabilidade_min:
        status = "ESTÁVEL"
    elif soma_total < colapso_min:
        status = "COLAPSANDO"
    else:
        status = "INSTÁVEL"

    print(f"Pacotes recebidos: {list(args)}")
    print(f"Transformados: {transformados}")
    print(f"Filtrados (primos > {limite_primo}): {filtrados}")
    print(f"Soma final: {soma_total}")
    print(f"Maior sequência consecutiva de primos: {seq_max}")
    print(f"\nStatus do Núcleo: {status}")

