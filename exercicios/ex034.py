"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%"""

salario = float(input('Digite o valor do seu salário R$: '))

salario_up = 1250 + (10/100 * 1250)
salario_down = 1250 + (15/100 * 1250)

if salario >= 1250:
    print(f'Seu novo salário será {salario_up}')
else:
    print(f'Seu novo salário será de {salario_down}')