# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: apos a sopa, a sacada da casa (frases que podem ser lidas de tras pra frente e vice-versa)

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
juntar = ''.join(palavras)
#inverso = ''
inverso = juntar[::-1]

'''
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]'
'''
    
print(juntar, inverso)

if inverso == juntar:
    print('É um palídromo!')
else:
    print(('Não é um palídromo.'))