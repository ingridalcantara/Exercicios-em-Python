"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - EQUILÁTERO: todos os lados iguais
    - ISÓSCELES: dois lados iguais
    - ESCALENO: todos os lados diferentes
"""

r1 = float(input('Digite o valor da reta 1: '))
r2 = float(input('Digite o valor da reta 2: '))
r3 = float(input('Digite o valor da reta 3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Podem formar um triângulo.')
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triângulo ISÓSCELES.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('É um triângulo ESCALENO.')
else:
    print('Não formam um triângulo.')