#Ler dois número onde o 1° vai ser o inicio do laço e o 2° vai ser o fim. 
#Validar os numeros de entrada

n1 = int(input("Digite o numero de inicio: "))
n2 = int(input("Digite o numero do final: "))

if n1 > n2:
    for i in range(n2, n1):
        print(i)
else:
    for i in range(n1, n2):
        print(i)