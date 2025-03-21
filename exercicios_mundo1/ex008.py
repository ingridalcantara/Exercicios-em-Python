# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
num = float(input('Digite um número: '))
cent = num * 100
mili = num * 1000
print(f'{num} metro(s) equivale a {cent} centímetros', end=' ')
print(f'enquanto {num} metro(s) é igual a {mili} milímetros')