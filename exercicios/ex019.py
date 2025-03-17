# um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

nome1 = input('aluno 1: ')
nome2 = input('aluno 2: ')
nome3 = input('aluno 3: ')
nome4 = input('aluno 4: ')

lista = [nome1, nome2, nome3, nome4]

escolhido = choice(lista)
print(f'o aluno escolhido é {escolhido}')