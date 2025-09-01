#Morador deseja descobrir quantas lampadas necessita para iluminar um comodo

print('Como descobrir quantas lâmpadas preciso para iluminar um cômodo da casa? ')

while True:
    try: 
        largura_comodo = float(input('Qual a largura do cômodo? '))
        break
    except:
      print('Digite um nº válido. ')

while True:
    try:
        comprimento_comodo = float(input('Qual o comprimento do cômodo? '))
        break
    except:
        print('Digite um nº válido.') 
    
while True:
    try:
        potencia_lampada_watts = float(input('Qual a potência da lâmpada em watts? '))
        break
    except:
        print('Digite um nº válido.') 

area = largura_comodo * comprimento_comodo
potencia_ideal = area * 3 #3w por m²
import math
quantidade_lampadas = math.ceil(potencia_ideal/potencia_lampada_watts) #1 bocal por m²

print('Resultado: ')
print(f'Área do cômodo: {area} m²')
print(f'Potência ideal: {potencia_ideal} watts')
print(f'Quantidade de lâmpadas necessárias: {quantidade_lampadas}') 