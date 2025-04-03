'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''
valores = list()
maior = menor = 0
for v in range(0,5):
    valores.append(int(input(f'Digite um valor na Posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'A lista de valores digitados é {valores}')
print(f'O maior valor digitado é {maior} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado é {menor} nas posições ', end='')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}...', end='')
        