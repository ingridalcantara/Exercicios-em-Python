'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    - quantas vezes apareceu o valor 9
    - em que posição foi digitado o primeiro valor 3
    - quais foram os números pares
'''
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))
numeros = (num1, num2, num3, num4)
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na {numeros.index(3,0)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os números pares são: ', end= '')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
# ou
'''
if num1 % 2 == 0:
    print(f'{num1}', end=' ')
if num2 % 2 == 0:
    print(f'{num2}', end=' ')
if num3 % 2 == 0:
    print(f'{num3}', end=' ')
if num4 % 2 == 0:
    print(f'{num4}', end=' ')'''