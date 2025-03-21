# faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
qtd_litro = area / 2
print(f'Para uma área de {area} metro(s) será necessário comprar {qtd_litro} litro(s) de tinta')