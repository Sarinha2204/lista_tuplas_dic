'''Leia uma frase do usu´ario e crie um dicion´ario que conte quantas vezes cada letra
aparece.'''

def contar_letras(frase):
    dicionario_letras = {}
    frase = frase.lower() 
    for letra in frase:
        if letra.isalpha():  
            if letra in dicionario_letras:
                dicionario_letras[letra] += 1
            else:
                dicionario_letras[letra] = 1
    return dicionario_letras
frase_usuario = input("Digite uma frase: ")
dicionario_resultado = contar_letras(frase_usuario)
print(f"Contagem de letras: {dicionario_resultado}")