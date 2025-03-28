# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
n = 'S'
media = quant = soma = maior = menor = 0
while n == 'S':
    num = int(input('Digite um número: '))
    n = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            num = maior
        if num < menor:
            menor = num
media = soma / quant
print(f'Você digitou {quant} e a média entre eles é {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')