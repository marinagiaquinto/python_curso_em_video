l1 = int(input('Digite um número: '))
l2 = int(input('Digite outro número: '))
l3 = int(input('Digite só mais um número: '))

if l1+l2 >= l3 and l2+l3 >= l1 and l3+l1 >= l2:
    print('Estas três medidas formam um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO (todos os lados iguais).')
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 ==l3 != l2:
        print('ISÓSCELES (dois lados iguais e um diferente).')
    else:
        print('ESCALENO (três lados diferentes).')
else:
    print('Estas três medidas NÃO podem formar um triângulo.')
