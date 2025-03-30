'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    - quantas vezes apareceu o valor 9
    - em que posição foi digitado o primeiro valor 3
    - quais foram os números pares
'''
cont9 = 0
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
num4 = int(input('Digite o quarto número: '))
numeros = (num1, num2, num3, num4)
if num1 == 9 or num2 == 9 or num3 == 9 or num4 == 9:
    cont9 += numeros
    print('O número 9 apareceu {} vezes' .format(cont9))