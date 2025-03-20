#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distancia = float(input('Qual a distância da sua viagem em km? '))

curta = distancia * 0.5
longa = distancia * 0.45

if distancia <=200:
    print('Você pagará R${:.2f}' .format(curta))
else:
    print('Você pagará R${:.2f}' .format(longa))