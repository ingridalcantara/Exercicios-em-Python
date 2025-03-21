# escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
km_perc = float(input('Quantos km percorridos: '))
dias = int(input('Quantos dias de aluguel? '))
preco = 60*dias + (0.15*km_perc)
print(f'o total a pagar será R$ {preco:.2f}')