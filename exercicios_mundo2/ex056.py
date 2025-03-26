"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    - a média de idade do grupo
    - qual é o nome do homem mais velho
    - quantas mulheres têm menos de 20 anos
"""

somaIdade = 0
mediaIdade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for prog in range(1,5):
    print(f'----- {prog}ª PESSOA -----')
    nome = str(input('Qual seu nome? ')).strip()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaIdade += idade

    if prog == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaIdade = somaIdade /4
print('A média da idade do grupo é de {} anos' .format(mediaIdade))
print(f'O nome do homem mais velho é {nomevelho} e ele tem {maioridadehomem}')
print(f'{totmulher20} mulheres tem menos de 20 anos.')