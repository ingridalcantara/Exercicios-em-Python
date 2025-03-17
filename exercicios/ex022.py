"""Crie um programa que leia o nome completo de uma pessoa e mostre: 
1 - o nome com todas as letras maisculas
2 - o nome com todas as letras minusculas
3 - quantas letras ao todo (sem considerar espaços)
4 - quantas letras tem o primeiro nome
"""

nome = str(input('Seu nome completo: ')).strip()

dividido = nome.split()


print(f'''1 - {nome.upper()}\n2 - {nome.lower()}\n3 - seu nome completo tem {len(nome)-nome.count(' ')} letras sem espaços\n4 - o primeiro nome tem {len(dividido[0])} letras''')