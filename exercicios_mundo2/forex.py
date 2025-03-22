"""inicio = int(input('Digite o numero inicial: '))
final = int(input('Digite o numero final: '))
passo = int(input('Digite o passo: '))

for c in range (inicio, final, passo):
    print(c)"
"""
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s = s + n
print('O somatório de todos os valores é {}'.format(s))