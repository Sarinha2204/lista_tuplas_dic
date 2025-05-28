'''Converta uma lista de temperaturas em Celsius para Fahrenheit com compreens˜ao
de listas.'''

temperaturas_celsius = [0, 20, 37, 100, -40]

temperaturas_fahrenheit = [(temp * 9/5) + 32 for temp in temperaturas_celsius] 


print(f"Temperaturas em Celsius: {temperaturas_celsius}")
print(f"Temperaturas em Fahrenheit: {temperaturas_fahrenheit}")
