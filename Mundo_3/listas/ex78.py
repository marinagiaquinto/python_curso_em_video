maior = menor = 0
valores= []

for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[0]
    else:
        if valores[c] >= maior:
            maior = valores[c]
        elif valores[c] <= menor:
            menor = valores[c]

print(f'Os valores digitados foram: {valores}')

print(f'O maior número digitado foi {maior} e está na(s) posição(ões)', end=' ')
for c, v in enumerate(valores):
    if v == maior:
        print(c,'... ', end='')

print(f'\nO menor número digitado foi {menor} e está na(s) posição(ões)', end=' ')
for c, v in enumerate(valores):
    if v == menor:
        print(c, '... ', end='')