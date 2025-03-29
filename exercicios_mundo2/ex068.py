# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''from random import randint
vitoria = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um número: '))
    tipo = str(input('Escolhar PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
    total = jogador + computador
    vitoria += 1
    print(f'Você escolheu {jogador} e o computador escolheu {computador}. O total foi {total}')
    if total % 2 == 0:
        print(f'O resultado é PAR.')
        while tipo in 'P':
            print('Você VENCEU!')
            break
    else:
        print(f'O resultado é ÍMPAR.')
        while tipo in 'I':
            print('Você GANHOU!!')
            break
    print(f'Você ganhou {vitoria} vezes.')
    print('='*60)'''
# o código acima deu errado
# o código abaixo deu certo
from random import randint
vitoria = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).upper().strip()[0]
    print(f'Você escolheu {jogador} e o computador escolheu {computador}. O total é de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            vitoria += 1
        else:
            print('Você perdeu.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            vitoria += 1
        else:
            print('Você perdeu.')
            break
    print('Tente novamente...')
print(f'Você ganhou {vitoria} vezes.')