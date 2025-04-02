'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
print('-' * 50)
print('{:^50}' .format('LISTAGEM DE PREÇOS'))
print('-' * 50)
t = ('Lápis', '1.75',
     'Borracha', '2',
     'Caderno', '15.90',
     'Estojo', '25',
     'Mochila', '120.32',
     'Livro', '34.90')
for item in range(0, len(t)):
    if item % 2 == 0:
        print(f'{t[item]:.<40}', end='')
    else:
        print(f'R${t[item]:>7}')
print('-' * 50)