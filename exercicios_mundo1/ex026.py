"""
Faça um programa que leia uma frase pelo teclado e mostre:
1 - quantas vezes aparece a letra "a"
2 - em que posição ela aparece a primeira vez
3 - em que posição ela aparece a última vez
"""

frase = str(input('Frase: ')).strip().upper()

print('a letra A aparece {} vezes'.format(frase.count('A')))
print('a primeira letra A aparece na {}a posição' .format(frase.find('A')+1))
print('a última letra A aparece na {}a posição' .format(frase.rfind('A')+1))