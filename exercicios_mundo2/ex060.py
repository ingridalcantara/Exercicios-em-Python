# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''from math import factorial
num = int(input('Digite um número para fatorar: '))
f = factorial(num)
print('A fatoração de {} é {}'.format(num, f))'''

num = int(input('Digite um número para fatorar: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print(f'{f}')