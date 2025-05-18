'''Solicite 5 n´umeros ao usu´ario e armazene em uma lista. Em seguida, imprima o
maior e o menor n´umero.
'''
# from random import randint
num = []

for i in range(5):
    x = int(input(f"Digite o {i+1}° número: "))
    #x = randint(1, 10)
    num.append(x)

maxi = max(num)
mini = min(num)


print(f"Maior número: {maxi}")
print(f'Menor número: {mini}')
