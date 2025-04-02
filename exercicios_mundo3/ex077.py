# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('jogar', 'trabalhar', 'dormir', 'gratis', 'aviao', 'ventilador', 'ar condicionado')
for item in palavras:
    print(f'\nNa palavra {item.upper()} temos ', end='')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end='')