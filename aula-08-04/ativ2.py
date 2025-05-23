'''Fazer ambas as repetições

*
**
***
****
*****

*****
****
***
**
*
'''

for i in range(1, 6):
    texto = ""
    for j in range(i):
        texto += "*"
    print(texto)


for i in range(5, 0, -1):
    texto = ""
    for j in range (i):
        texto += f"{i}"
    print(texto)
    


for i in range(6):
    for j in range(1, i):
        print(j, end=' ')
    print('')