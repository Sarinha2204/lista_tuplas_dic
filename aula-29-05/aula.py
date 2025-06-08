resultado = 0

def soma (a, b):
    print(a + b)
    
def sub (a, b):
    resultado = a - b
    print(resultado)
    
def mult (a, b):
    resultado = a * b
    print(resultado)
    
def div (a, b):
    if b > 0:
        resultado = a / b
        print(resultado)
    print("Divisão por zero não é permitida")


soma(2, 3)
sub(2, 3)
mult(2, 3)
div(2, 0)