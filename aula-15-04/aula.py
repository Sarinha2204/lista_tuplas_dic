'''
1-var de controle
2-condição de parada
3-att da var de controle


#1° = var de controle
i=0

#2° = condição de parada

while i< 50:
    if i % 2 = 0:
    print(f'i = {i}')

#3° = att da var
    i = i + 1 #incremento
'''    
#criar um laco de repeticao com while que dependa da reaposta do user para continuar o laco

resp = 's'
while resp == 's':
    print('ainda estou repetindo...')
    resp = input('deseja continuar? s = sim / n = não ')
    resp = resp.lower()
    if resp == 's' or resp == 'n':
        break
        
print('terminei!')