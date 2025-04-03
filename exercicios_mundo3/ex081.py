'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
    - Quantos números foram digitados
    - A lista de valores, ordenada de forma decrescente
    - Se o valor 5 foi digitado e está ou não na lista
'''
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    numeros.append(n)
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'A lista tem {len(numeros)} elementos.')
print(f'A lista digitada é ', end= '')
numeros.sort(reverse=True)
print(numeros)
if 5 in numeros:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')