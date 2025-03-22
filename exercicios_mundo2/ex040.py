""" Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:"
    - média abaixo de 5.0: REPROVADO
    - média entre 5.0 e 6.9: RECUPERAÇÃO
    - média 7.0 ou superior: APROVADO
"""
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) /2

if media < 5:
    print('Sua média foi {:.1f}. Você foi REPROVADO!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {:.1f}. Você está em RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('Sua média foi {:.1f}. Você está APROVADO!!' .format(media))