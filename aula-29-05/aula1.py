def func1(x, y):
    h = [x**2 for x in func2(y)]
    return h

def func2(x):
    r = []
    for i in func3(x, x*2, x*3):
        r.append(i**0.5)
    return r

def func3(a, d, c):
    lista = [x**2 for x in [a, d, c] if x % 3 == 0]
    return (lista)

print(func1(2, 3))