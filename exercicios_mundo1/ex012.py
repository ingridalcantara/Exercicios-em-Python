# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Digite o valor: '))
novo_preco = preco - (5/100)*preco
print(f'Para o valor de R$ {preco}, seu novo valor com 5% de desconto será de R$ {novo_preco:.2f}')