'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
    - Qual é o total gasto na compra.
    - Quantos produtos custam mais de R$1000.
    - Qual é o nome do produto mais barato.
'''
total = mil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        mil += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
    print('='*30)
print('~'*30)
print(f'O total gasto foi de R${total:.2f}')
print(f'{mil} produtos custam mais de R$1000')
print(f'{barato} é o produto mais barato e custa R${menor:.2f}')