"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    - abaixo de 18.5: abaixo do peso
    - entre 18.5 e 25: peso ideal
    - 25 até 30: sobrepreso
    - 30 até 40: obesidade
    - acima de 40: obesidade mórbida
"""

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é {:.2f} e você está ABAIXO DO PESO.' .format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.2f} e você está no PESO IDEAL.' .format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f} e você está no SOBREPESO.' .format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f} e você está na OBESIDADE.' .format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f} e você está na OBESIDADE MÓRBIDA.' .format(imc))