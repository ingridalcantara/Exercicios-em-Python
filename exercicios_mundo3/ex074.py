'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint
num1 = randint(0, 10)
num2 = randint(0, 10)
num3 = randint(0, 10)
num4 = randint(0, 10)
num5 = randint(0, 10)
numeros = (num1, num2, num3, num4, num5)
print('Os números sorteados são: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')
