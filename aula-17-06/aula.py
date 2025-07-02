from functools import reduce
# *args são convenções em python que permitem que funções recebam um 
# número variável de parametros.


#Contabilizar o numero de sublistas dentro de args utilizando RECURSAO
def sub_listas(lista):
    contador = 0
    for arg in lista:
        if isinstance(arg, list):
            contador += 1 + sub_listas(arg)
    return contador


#Contabilizar o numero de sublistas dentro de args utilizando REDUCE
def count_sublist_reduce(*args):
    return reduce(lambda count, item: count + (1 if isinstance(item, list) else 0), args, 0)


#Contabilizar o numero de sublistas dentro de args utilizando COMPREHENSION
lista = [2, 3, 4, 5, 6, [7, 8, 9], [10, 11,[12, 13]]]
print(f"Sublistas diretas: {sub_listas(lista)}")


def minha_funcao(a, b, *args):
    
    print(f"Argumentos recebidos: {args}")
    
    print(sub_listas(args))
    
minha_funcao(2, 3, 4, 5, 6, [7, 8, 9], [10, 11,[12, 13]])




#Contabilizar o numero de sublistas dentro de args utilizando PARAMETROS NOMEADOS 
def soma(a, b, c):
    pass

soma(c= 2, a = 3, b = 1)


def funcao_completa(param_obg, *args, **kwargs):
    print(f"Parametros obrigatorios: {param_obg}")
    print(f"Args extras: {args}")
    print(f"Kwargs extras {kwargs}")


funcao_completa("v1", "v2", "extra1", "extra2", nome= "sara", idade = 18)


#implementar umac calculadora que leia dois tipos (soma, multiplicação), lista de números, 
#exibir_detalhes= True, caso seja false retornar o resultado final

def calculadora(tipo, numeros, exibir_detalhes=False):
    if tipo == "soma":
        resultado = sum(numeros)
    elif tipo == "multiplicacao":
        resultado = reduce(lambda x, y: x * y, numeros)
    else:
        raise ValueError("Tipo inválido. Use 'soma' ou 'multiplicacao'.")

    if exibir_detalhes:
        print(f"Tipo: {tipo}")
        print(f"Números: {numeros}")
        print(f"Resultado: {resultado}")

    return resultado
