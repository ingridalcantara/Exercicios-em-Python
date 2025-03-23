# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year

for ano in range(0,7):
    nascimento = int(input('Digite seu ano de nascimento: '))

if ano_atual - nascimento <= 18:
    print('')