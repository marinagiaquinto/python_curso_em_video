tot = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        cont +=1
        tot += n
print (f'Foram digitado {cont} números pares e a soma entre eles é {tot}')
