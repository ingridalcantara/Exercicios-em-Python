'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    entrada = int(input('Digite um número entre 0 e 20: '))
    if 0 <= entrada <= 20:
        print('Você digitou', num[entrada])
        pergunta = ' '
        while pergunta not in 'SN':
            pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if pergunta == 'N':
            print('Programa encerrado.')
            break
    else:
        print('Tente novamente.', end=' ')
# ------------------------------------------------------------------------------------------
'''
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 
       'dezenove', 'vinte')

while True:
    entrada = int(input('Digite um número entre 0 e 20: '))
    if 0 <= entrada <= 20:
        print(f'Você digitou o número {num[entrada]}')
    else:
        print('Número inválido. Tente novamente.', end=' ')
        continue
    
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = input('Quer continuar? [S/N] ').strip().upper()[0]
    if pergunta == 'N':
        break
print('Programa encerrado.') '''
