# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for par in range (0,6):
    num = int(input('Escolha um número: '))
    if (num%2) == 0:
        soma = soma + num
print(f'A soma é {soma}')