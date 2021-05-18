from random import randint

sorteio = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Olá! Estes são os cinco números sorteados: {sorteio}')

print(f'O MAIOR número sorteado foi o {max(sorteio)} e o MENOR {min(sorteio)}.')