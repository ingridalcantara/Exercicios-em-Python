# crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
num = int(input('Digite um número: '))
dobro = num *2
triplo = num *3
raiz = pow(num, 1/2)
print(f'O dobro de {num} é {dobro}, enquanto o triplo é {triplo} e a raiz quadrada é {raiz:.3f}')