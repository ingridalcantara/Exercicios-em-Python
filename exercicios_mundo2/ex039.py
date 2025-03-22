"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    - se ele ainda vai se alistar ao serviço militar
    - se é a hora de se alistar
    - se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

ano = int(input('Informe seu ano de nascimento: '))

ano_atual = date.today().year

ano_alistamento = ano_atual - ano

if ano_alistamento < 18:
    print('Ainda falta {} anos para você se alistar.' .format(18-(ano_atual - ano)))
elif ano_alistamento > 18:
    print('já passou do tempo do alistamento')
else:
    print('Já é hora de se alistar.')