# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar, considerando US$ 1 = R$ 5,74
din = float(input('quanto você tem em R$? '))
dolar = din / 5.74
print(f'Com R${din} você pode comprar US${dolar:.2f}')