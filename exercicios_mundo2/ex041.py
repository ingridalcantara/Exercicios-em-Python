"""
a Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    - até 9 anos: MIRIM
    - até 14 anos: INFANTIL
    - até 19 anos: JUNIOR
    - até 20 anos: SÊNIOR
    - acima: MASTER
"""

from datetime import date

ano = int(input('Qual seu ano de nascimento? '))

ano_atual = date.today().year

ano_base = ano_atual - ano

if ano_base <= 9:
    print(f'Você tem {ano_base} anos. Sua categoria é MIRIM.')
elif ano_base > 9 and ano_base <= 14:
    print(f'Você tem {ano_base} anos. Sua categoria é INFANTIL.')
elif ano_base > 14 and ano_base <= 19:
    print(f'Você tem {ano_base} anos. Sua categoria é JÚNIOR.')
elif ano_base > 19 and ano_base <= 20:
    print(f'Você tem {ano_base} anos. Sua categoria é SÊNIOR.')
elif ano_base > 20:
    print(f'Você tem {ano_base} anos. Sua categoria é MASTER.')