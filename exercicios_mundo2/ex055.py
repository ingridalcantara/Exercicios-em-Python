# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa em kg: '))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg' .format(maior))
print('O menor peso lido foi de {}Kg' .format(menor))