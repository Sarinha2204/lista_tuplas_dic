'''Dada uma lista de inteiros, crie uma fun¸c˜ao que identifique os n´umeros que aparecem
mais de uma vez e quantas vezes cada um aparece.'''

def contar_repeticoes(lista):
    contagem = {}
    for numero in lista:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    repetidos = {num: count for num, count in contagem.items() if count > 1}
    return repetidos

lista_exemplo = [1, 2, 3, 2, 4, 5, 1, 6, 3] 
print(contar_repeticoes(lista_exemplo))