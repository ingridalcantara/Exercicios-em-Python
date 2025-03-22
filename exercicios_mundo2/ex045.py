# Crie um programa que faça o computador jogar Jokenpô com você. -> pedra papel tesoura

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('Escolha uma opção...')
print('[0] - PEDRA\n[1] - PAPEL\n[2] - TESOURA')
opcao = int(input('Qual sua escolha? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-='*15)
print('O jogador escolheu {}' .format(itens[opcao]))
print('O computador escolheu {}' .format(itens[computador]))
print('-='*15)

if computador == 0: # computador joga PEDRA
    if opcao == 0:
        print('EMPATE')
    elif opcao == 1:
        print('Jogador ganhou!')
    elif opcao == 2:
        print('Computador ganhou!')
elif computador == 1: # computador joga PAPEL
    if opcao == 0:
        print('Computador ganhou!')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('Jogador ganhou!')
elif computador == 2: # computador joga TESOURA
    if opcao == 0:
        print('Jogador ganhou!')
    elif opcao == 1:
        print('Computador ganhou!')
    elif opcao == 2:
        print('EMPATE')
else:
    print('Opção inválida.')