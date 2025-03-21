# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt

cat_opo = float(input('Cateto oposto: '))
cat_adj = float(input('Cateto adjacente: '))

hip = sqrt(cat_opo**2 + cat_adj**2)

print(f'a hipotenusa é {hip:.2f}')