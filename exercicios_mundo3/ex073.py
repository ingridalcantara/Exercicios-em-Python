'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    - apenas os 5 primeiros colocados
    - os últimos 4 colocados da tabela
    - uma lista com os times em ordem alfabética
    - em que posição na tabela está o time do Flamengo
'''
times = ('Fortaleza', 'Juventude', 'Cruzeiro', 'Grêmio', 'Flamengo', 'Internacional', 'São Paulo', 'Sport', 'Bahia', 'Botafogo', 'Ceará', 'Corinthians', 'Palmeiras', 'Bragantino', 'Santos', 'Vasco da Gama', 'Atlético-MG', 'Mirassol', 'Fluminense', 'Vitória')
print('Os cinco primeiros colocados são: ', times[0:5])
print('Os quatro últimos da tabela são: ', times[16:])
for c in times:
    print(sorted(times))
    break
