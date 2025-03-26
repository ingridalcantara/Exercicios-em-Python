# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
totmaior = 0
totmenor = 0

for ano in range(1,8):
    nascimento = int(input(f'Ano de nascimento da {ano}ª pessoa: '))
    
    if ano_atual - nascimento <= 18:
        totmenor = totmenor + 1
    else:
        totmaior += 1

print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.')