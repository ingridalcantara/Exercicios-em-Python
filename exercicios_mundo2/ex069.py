'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    a) quantas pessoas tem mais de 18 anos
    b) quantos homens foram cadastrados
    c) quantas mulheres tem menos de 20 anos
'''
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    print('CADASTRADO COM SUCESSO!')
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        break
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
print(f'Ao total, há {tot18} pessoas com mais de 18 anos.')
print(f'Ao total, {totH} homens foram cadastrados.')
print(f'Ao total, {totM20} mulheres de 20 anos.')