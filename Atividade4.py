#Em uma turma os alunos realizam duas avaliações obrigatórias e uma opcional
print('Sistema de notas do semestre: ' )

while True:
    try:
        nota1 = float(input('Digite a nota da 1ª avaliação: '))
        break
    except:
              print('Digite um nº válido. ')

while True:
    try:  
        nota2 = float(input('Digite a nota da 2ª avaliação: '))
        break
    except:
           print('Digite um nº válido. ')

while True:
    try:
        nota3 = float(input('Digite a nota da 3ª avaliação (optativa): ')) 
        break
    except:
        print('Digite um nº válido. ')

notas = [nota1, nota2]

if nota3 > min(notas):
     menor_indice = notas.index(min(notas))
     notas[menor_indice] = nota3

media = sum(notas)/len(notas)
print (f'A média final do aluno é igual a {media}. ')

print('Situação do aluno: ')
if media >=6:
    print('Aprovado ')
elif media >=3 and media <6:
     print('Recuperação ')
else:
     print('Reprovado ')
     