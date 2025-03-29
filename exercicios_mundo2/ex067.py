# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
from time import sleep

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    print('-'*40)
    for n in range(1,11):
        print(f'{num} x {n} = {num*n}')
    print('-'*40)
    sleep(1)
print('ACABOU!!')