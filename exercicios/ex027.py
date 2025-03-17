# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
nome_div = nome.split()
print(f'Seu nome é {nome_div[0]} e sobrenome é {nome_div[len(nome_div)-1]}')