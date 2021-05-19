v1 = int(input('Digite o primeiro valor: '))

maior = v1

v2 = int(input('Digite o segundo valor: '))

if v2>maior:
    menor = v1
    maior = v2
else:
    menor = v2

v3 = int(input('Digite o terceiro valor: '))

if v3>maior:
    maior = v3
if v3<menor:
    menor = v3

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
