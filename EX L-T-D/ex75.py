'''Armazene dados de uma enquete com tuplas (nome, voto) em uma lista e conte
os votos usando um dicion´ario.
'''

def contar_votos(enquete):
    votos = {}
    for nome, voto in enquete:
        if voto in votos:
            votos[voto] += 1
        else:
            votos[voto] = 1
    return votos
enquete = [('Sara', 'Maçã'),('Luiz', 'Banana'),('Luana', 'Maçã'),('Raiany', 'Laranja'),('Yasmin', 'Banana'),('Gabriel', 'Maçã'),('Matheus', 'Laranja'),('Duda', 'Banana'),('Igor', 'Maçã'),('Mafer', 'Laranja')]
resultado_votos = contar_votos(enquete)
print(f"Resultado da enquete: {resultado_votos}")