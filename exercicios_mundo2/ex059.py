'''
Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep
primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
resposta = 0
while resposta != 5:
    print('''Escolha uma opção:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa''')
    resposta = int(input('Digite o número da opção: '))
    print('='*30)
    if resposta == 1:
        soma = primeiro + segundo
        print(f'A soma entre {primeiro} e {segundo} é {soma}')
        print('='*30)
    elif resposta == 2:
        multiplicacao = primeiro * segundo
        print(f'A multiplicação entre {primeiro} e {segundo} é {multiplicacao}')
        print('='*30)
    elif resposta == 3:
        if primeiro > segundo:
            print(f'Entre {primeiro} e {segundo}, o maior valor é {primeiro}')
            print('='*30)
        else:
            print(f'Entre {primeiro} e {segundo}, o maior valor é {segundo}')
            print('='*30)
    elif resposta == 4:
        print('Informe os novos números...')
        primeiro = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))
    elif resposta == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção errada. Tente novamente.')
        print('='*30)
print('Fim do programa! Volte sempre!')