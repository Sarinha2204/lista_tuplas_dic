'''Crie uma lista com n´umeros de 1 a 100 e filtre os m´ultiplos de 3.'''

lista_numeros = list(range(1, 101))

multiplos = [num for num in lista_numeros if num % 3 == 0]
print(multiplos)