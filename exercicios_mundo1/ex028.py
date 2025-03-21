# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# o programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

computador = randint(0,5)

print('Adivinha em que número estou pensando...')
resp = int(input('R: '))
if resp == computador:
    print('Acertou!!')
else:
    print(f'Errou! Estou pensando no número {computador}')