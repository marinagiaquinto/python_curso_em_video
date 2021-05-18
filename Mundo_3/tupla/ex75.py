print('DE 1 A 10')
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')), int(input('Digite um último número: ')))


nove = 0
par = 0
tres = 0

for c in numeros:
    if c == 9:
        nove += 1


for c in numeros:
    if c == 3:
        tres = numeros.index(3) + 1
    else:
        tres = 0



print('-'*30)
print(f'Os números digitados foram {numeros}')
print('-'*30)
print(f'O número nove apareceu {nove} vezes')
print('-'*30)
print(f'O valor 3 foi digitado pela primeira vez na posição {tres}')
print('-'*30)


print(f'Os número pares foram: ', end='')

for c in numeros:
    if c%2 == 0:
        print(c, end=' ')


