nome = 'Joao','Jose'

print(nome)

cliente = []
while True:
    try:
        num = int(input('Digite o Nº: '))
        cliente.append(num)
        sair = input('Deseja adicionar mais um nº? (S/N)').upper().strip()
        if sair == 'N':
            break
    except:
        print('Digite um Nº válido.')





for i in cliente:
    print(i)

telefone = 2199563215
idade = 32
cliente.append(telefone)

print('1\n2\n3\n4')

while True:
    try:
        opcao = int(input('opcao: '))
        if opcao in [1,2,3,4]:
            print('opcao ok')
            break
        else:
            print('opcao invalida')
    except:
        print('Digite um nº valido: ')

cadastro = []
int(input('Informe quantos produtos deseja cadastrar: '))
            
print('produto')
while True:
    try:
        produto = input('Digite o nome o produto: ')
        cadastro.append(produto)
        sair = input('Deseja adicionar mais um produto? (S/N)').upper().strip()
        if sair == 'N':
            break
    except:
        print('Digite um dado válido.')

print('valor_produto')
while True:
    try:
        valor_produto = float(input('Digite o valor do produto: '))
        cadastro.append(valor_produto)
        sair = input('Deseja adicionar mais um valor? (S/N)').upper().strip()
        if sair == 'N':
            break
    except:
        print('Digite um nº válido.')

for i in cadastro:
    print(f'')



