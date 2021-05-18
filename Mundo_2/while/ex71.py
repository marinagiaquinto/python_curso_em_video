cinquenta = vinte = dez = um = 0

v1 = (int(input('Qual valor você quer sacar? ')))

while True:
    while v1 >= 50:
        v1 = v1 - 50
        cinquenta +=1
    while v1 >= 20:
        v1 = v1 - 20
        vinte += 1
    while v1 >= 10:
        v1 = v1 - 10
        dez += 1
    while v1 >= 1:
        v1 = v1 - 1
        um += 1
    if v1 == 0:
        break


print(f'Você levará o total:')
print(f'{cinquenta} cédula(s) de R$50')
print(f'{vinte} cédula(s) de R$20')
print(f'{dez} cédula(s) de R$10')
print(f'{um} cédula(s) de R$1')