distancia = float(input('Digite a distância da sua viagem em km/h: '))
if distancia <= 200:
    valor = distancia*0.50
else:
    valor = distancia*0.45
print(f'O valor da sua viagem será {valor :.2f} reais')