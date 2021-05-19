dia = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos quilometro rodou com o automovel? '))
tot_dia = dia * 60
tot_km = km * 0.15
tot = tot_dia + tot_km
print(f'Pelos {dia} dias percorridos, pagará {tot_dia}.')
print(f'Pelos {km} quilometros percorridos, pagará {tot_km}.')
print(f'O que totaliza uma despeza de {tot}, pela sua jorgana.')