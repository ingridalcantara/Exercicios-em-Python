# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (11-1) * razao

for pa in range (primeiro, decimo, razao):
    print(pa, end = '->')
print('ACABOU!')