num = [[],[]]

for c in range(1,8):
    numero = int(input(f'Digite o {c}º número: '))
    if numero%2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)

num[0].sort()
num[1].sort()

print(f'Os números PARES digitados foram {num[0]} e os ÍMPARES {num[1]}')
