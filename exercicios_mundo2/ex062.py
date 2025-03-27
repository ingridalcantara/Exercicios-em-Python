# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos. 
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
termo = primeiro
cont = 1
total = 0
pergunta = 10
while pergunta != 0:
    total = total + pergunta
    while cont <= total:
        print('{} -> '. format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    pergunta = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print(f'PA finalizada com {total} termos mostrados.')