'''Solicite ao usuário 10 números, armazene em uma lista e remova todos os números
pares usando remove.'''

num = []

for i in range(5):
    x = int(input(f"Digite o {i+1}° número: "))
    num.append(x)
    
for n in num[:]:
    if n % 2 == 0:
        num.remove(n)

print("Lista sem os números pares:", num)