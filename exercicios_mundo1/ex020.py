# O professor quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

nome1 = input('aluno 1: ')
nome2 = input('aluno 2: ')
nome3 = input('aluno 3: ')
nome4 = input('aluno 4: ')

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print('a ordem de apresentação será ')
print(lista)