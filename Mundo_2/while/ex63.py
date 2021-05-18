print('Sequência de Finonacci')
print('-'*20)

quant = int(input('Quantos termos deseja ver da Sequência de Fibonacci? '))
x = 0
y = 1
s = 0
c = 3

print('0 1', end=' ')

while c <= quant:
 s = x+y
 print(s, end=' ')
 x=y
 y=s
 c+= 1
