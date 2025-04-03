'''lanche = ['pudim', 'bolo', 'suco', 'pizza']
lanche.append('cookie') # adiciona um item no final da lista
lanche.insert(0, 'bolacha') # adiciona um item na posição 0
lanche.remove('pudim') # exclui o item
del lanche[2] # exclui o item que ta na posição 2
lanche.pop() # exclui o ultimo item ou ----- 'lanche.pop(2)' exclui o item que ta na posição 2
print(lanche)'''

'''valores = list(range(4,11)) # cria valores dentro de uma lista'''
'''valores = [3,5,2,8,1,6]
valores.sort() # orderna os valores'''
'''valores.sort(reverse=True) # ordena os valores ao contrario'''

'''
valores  = []
valores.append(9)
valores.append(7)
valores.append(2)'''
'''for v in valores:
    print(f'{v}...', end='')'''
'''for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')'''
'''
# para ler valores pelo teclado
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
'''

# ATRIBUIÇÃO DE DUAS LISTAS
a = [2, 3, 5, 8]
b = a[:]    # b cria uma cópia de a
'''b = a    # b é igual a a'''
b[2] = 8    # atribui o 8 na posição 2
print(f'Lista de A: {a}')
print(f'Lista de B: {b}')