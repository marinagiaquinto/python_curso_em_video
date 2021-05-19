n1 = float(input('Digite um número: '))
n2 = float(input('Digite um segundo número:'))
n3 = float(input('Digite o terceiro número: '))

if n1<n2+n3 and n2<n3+n1 and n3<n1+n2:
    print('Eles podem formar um triângulo')
else:
    print('Eles não podem formar um triângulo')