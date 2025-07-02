'''Leia 5 números do usuário e verifique se cada um deles é maior que 10.'''

#from random import randint

num = []
maior = 0

for i in range(5):
    x = int(input(f"Digite o {i+1}° número: "))
    #x = randint(1, 5)
    num.append(x)
    
    if x >= 10:
        maior += 1
print(num)
print(f"Dentre os 5 número digitados, {maior} são maiores que 10")