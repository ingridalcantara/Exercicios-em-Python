"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
    - 1 para binário
    - 2 para octal
    - 3 para hexadecimal
"""

num = int(input('Digite um número para converter: '))
base = int(input('Qual a base de conversão?\nDigite [1] para binário\nDigite [2] para octal\nDigite [3] para hexadecimal\nResposta: '))


if base == 1:
    print('o número {} para binário é {}' .format(num, bin(num)[2:]))
elif base == 2:
    print('o número {} para octal é {}' .format(num, oct(num)[2:]))
elif base == 3:
    print('o número {} para hexadecimal é {}' .format(num, hex(num)[2:]))
else:
    print('opção inválida.')