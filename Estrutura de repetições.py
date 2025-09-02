#While com condição
#Exemplo:
'''contador = 1
while contador <=5:
    print(f'Contador = {contador}')
    contador +=1

#Validação com while
#Exemplo:
numero = ''
while numero != '10':
    numero = input('Digite um numero maior que 10: ').strip()   
    if numero != '10':
        print('Digite novamente: ')  
print('Numero correto!')

#Validação com while
#Exemplo:
'''senha = ''
while senha != '1234':
    numero = input('Digite a senha: ').strip()   
    if senha != '1234':
        print('Digite novamente: ')  
print('Numero correto!')'''


#For e range
#Exemplo
for i in range(0,31,10):
    print(i)'''

while True:
    try:
        numero = int(input('Digite um nº maior que 10: '))
        if numero <=10:
            print('Numero incorreto. Digite novamente:')
        break
    except:
        print('Digite novamente:')

#Tabuada
for i in range(1,11):
    print(f'7 x {i} = {7*i}')


    