n = int(input('Digite o primeiro número: '))
razao = int(input('Digite a razão em que será realizada a P.A: '))
print(n, end=' ')

for c in range(1,10):
    n += razao
    print(n, end=' ')


##OR:  for c in range(n, 10, razao)   !!!!!!!!!