numeros = [[],[],[]]
tot_par = tot_coluna = maior = 0

for linha in range(0,3):
    for coluna in range(0,3):
        numeros[linha].append(int(input(f'Digite um valor p casa [{linha,coluna}]: ')))
        if numeros[linha][coluna] %2 == 0:
            tot_par += numeros[linha][coluna]
        if coluna == 2:
            tot_coluna += numeros[linha][coluna]
        if linha == 1:
            if coluna == 0:
                maior = numeros[1][0]
            else:
                if numeros[1][1] > maior:
                    maior = numeros[1][1]
                elif numeros[1][2] > maior:
                    maior = numeros[1][2]

print()
print('-'*3, 'MATRIZ', '-'*3)
print(numeros[0])
print(numeros[1])
print(numeros[2])
print('-'*15)
print()

print(f'A soma de todos os valores pares digitados: {tot_par}')
print(f'A soma dos valores da terceira coluna: {tot_coluna}')
print(f'O maior valor da segunda linha: {maior}')