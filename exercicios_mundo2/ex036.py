# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salário? R$'))
tempo = float(input('Em quantos anos você vai pagar? '))

prestacao = valor / (tempo*12)
sal_exc = (30/100 * salario)

print('O valor da prestação será R${:.2f}' .format(prestacao))

if prestacao > sal_exc:
    print('\033[1;41mEmpréstimo negado!\033[m')
else:
    print('\033[1;33;42mEmpréstimo aprovado!\033[m')