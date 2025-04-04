'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
numeros = []
par = list()
impar = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Lista original: {numeros}')
print(f'Lista par: {par}')
print(f'Lista ímpar: {impar}')