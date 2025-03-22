"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
    1 - à vista dinheiro/cheque: 10% de desconto
    2 - à vista no cartão: 5% de desconto
    3 - em até 2x no cartão: preço normal
    4 - 3x ou mais no cartão: 20% de juros
"""

valor = float(input('Digite o valor do produto: R$'))
forma_pagamento = int(input('Escolha a forma de pagamento...\n[1] - à vista dinheiro/cheque: 10% de desconto\n[2] - à vista no cartão: 5% de desconto\n[3] - em até 2x no cartão: preço normal\n[4] - 3x ou mais no cartão: 20% de juros\nRESPOSTA: '))

vista_din = valor - (10/100 * valor)
vista_cartao = valor - (5/100 * valor)
parc2_cartao = valor / 2
num_parc = 1

if forma_pagamento == 1:
    print('Você tem 10% de desconto, então pagará {:.2f}' .format(vista_din))
elif forma_pagamento == 2:
    print('Você tem 5% de desconto, então pagará {:.2f}' .format(vista_cartao))
elif forma_pagamento == 3:
    print('Você tem 5% de desconto, então pagará {:.2f}' .format(parc2_cartao))
elif forma_pagamento == 4:
    num_parc = int(input('Em quantas vezes você quer parcelar? '))

parc_cartao = (valor + (20/100 * valor)) / num_parc

if forma_pagamento == 4:
    print('Você pagará {:.2f} por mês. Então pagará R${:.2f} ao total' .format(parc_cartao, num_parc*parc_cartao))