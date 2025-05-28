'''Crie uma função que retorne o segundo maior número de uma lista.'''

def segundo_maior(lista):
    if len(lista) < 2:
        return None
    primeiro_maior = segundo_maior = float('-inf')
    
    for numero in lista:
        if numero > primeiro_maior:
            segundo_maior = primeiro_maior
            primeiro_maior = numero
        elif primeiro_maior > numero > segundo_maior:
            segundo_maior = numero
            
    return segundo_maior if segundo_maior != float('-inf') else None