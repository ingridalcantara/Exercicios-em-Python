# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' -> FIM')