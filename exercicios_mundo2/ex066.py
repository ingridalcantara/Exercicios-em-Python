# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
cont = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print('ACABOU!')
print('~'*75)
print('='*15,f'Você digitou {cont} números e a soma deles é {soma}.', '='*15)
print('~'*75)
