'''
Recursividade:
A recursividade é uma técnica de programação onde uma função chama a si mesma 
para resolver um problema. 

Principais caracteristicas
- Caso base: condição que encerra a recursão(chamadas infinitas)
- Caso recursivo: chama a si mesma com um problema menor ou modificado.
'''

def func(x):
    print(x)
    if x < 1:
        return 0
    return x + func(x - 1)
    
#3 + func(2)
#2 + func(1)
#1 + 0
print(func(3))


#Fatorial de 5

'''def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)'''
    
def fatorial(x):
    if x == 1:
        return 1
    return x * fatorial(x - 1)

print(fatorial(5))


#Fibonacci 1 1 2 3 5 8 13
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)
    
print(fibonacci(7))

