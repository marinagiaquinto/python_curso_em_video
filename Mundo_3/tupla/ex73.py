brasileirao = ('Flamengo','Internacional','Atlético Mineiro','São Paulo',
                'Fluminense','Grêmio','Palmeiras','Santos','Atlético Paranaense',
                'Bragantino','Ceará','Corinthians','Atlético de Goias','Bahia',
                'Sport Recife','Fortaleza','Vasco','Goiás','Coritiba','Botafogo')


print(f'Times Brasileirão 2020: {brasileirao}')
print('-'*30)
print(f'Os 5 primeiros colocados no campeonato, são: {brasileirao [:5]}')
print('-'*30)
print(f'Os 4 últimos colocados: {brasileirao [16:]}')
print('-'*30)
print(f'Os times em ordem alfabética: {sorted(brasileirao)}')
print('-'*30)
print(f'O São Paulo ocupa a {brasileirao.index("São Paulo") + 1}ª posição.')
print('-'*30)
