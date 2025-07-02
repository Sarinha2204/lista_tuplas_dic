'''Dada uma lista de tuplas (cidade, temperatura), crie um dicion´ario que armazene
a m´edia de temperaturas por cidade.'''

def media_temperaturas(cidades_temperaturas):
    dicionario_media = {}
    contagem = {}
    
    for cidade, temperatura in cidades_temperaturas:
        if cidade not in dicionario_media:
            dicionario_media[cidade] = 0
            contagem[cidade] = 0
        dicionario_media[cidade] += temperatura
        contagem[cidade] += 1
    
    for cidade in dicionario_media:
        dicionario_media[cidade] /= contagem[cidade]
    
    return dicionario_media


cidades_temperaturas = [('São Paulo', 25),('Rio de Janeiro', 30),('São Paulo', 28),('Belo Horizonte', 22),('Rio de Janeiro', 32),('Belo Horizonte', 24)  ]

resultado_media = media_temperaturas(cidades_temperaturas)
print(f"Média de temperaturas por cidade: {resultado_media}")