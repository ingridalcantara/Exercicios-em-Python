# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número para ver sua tabuada: '))

for tabuada in range (0, 11):
    print('{} x {} = {}' .format(num, tabuada, num*tabuada))