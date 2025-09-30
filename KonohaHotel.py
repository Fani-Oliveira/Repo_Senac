print('Olá, seja bem vindo ao Konoha Hotel')
print('Escolha o tipo de quarto: ')
print('1- Quarto Genin: R$120,00 por noite\n2- Quarto Jounin: R$180,00 por noite\n3- Suíte Hokage: R$250,00 por noite')

#Escolher tipo de quarto
while True:
    try:
        tipo_quarto = int(input('Digite o nº do quarto escolhido: '))
        break
    except:
        print('Digite um nº válido. ')

nome = input('Informe seu nome: ')
noites = int(input('Informe quantas noites deseja ficar: '))
#Preço do quarto por noite:
if tipo_quarto == 1: 
    preco_noite = 120 
    nome_quarto = 'Quarto Genin'
elif tipo_quarto == 2:
    preco_noite = 180
    nome_quarto = 'Quarto Jounin'
elif tipo_quarto == 3:
    preco_noite = 250
    nome_quarto = 'Suíte Hokage'
else:
    print('Quarto escolhido')

valor_estadia = preco_noite * noites
print(f'O valor da estadia é {valor_estadia} reais.')
print(f'O quarto escolhido foi {nome_quarto}, no período de {noites} dias, com o valor total de {valor_estadia} reais.')
print('Obrigado por escolher o Konoha Hotel.\nDesejamos uma ótima estadia!')
