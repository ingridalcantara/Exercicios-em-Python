'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
entrada = int(input('Digite um número entre 0 e 20: '))
print('Você digitou', num[entrada])
