# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. 

from random import randint
computador = randint(0,10)
print('Adivinha em que número estou pensando...')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente.')
        else:
            print('Menos... tente novamente.')
print(f'Acertou com {palpite} tentativas. Parabéns!')