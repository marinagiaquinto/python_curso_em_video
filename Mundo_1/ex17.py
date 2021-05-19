from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente: '))
print(f'A hipotenusa vale {hypot(co, ca) :.2f}')


'''from math import sqrt
co = (float (input('Cateto oposto: ')))
ca = (float (input('Cateto adjacete: ')))
hip = (sqrt(co**2 + ca**2))
print(f'A hipotenusa vale: {hip :.2f}')


quadrado da hipotenusa é igual a soma dos quadrados dos catetos
portanto, a hipotenusa é a raiz quadrada da soma dos quadrados dos catetos
triangulo retângulo é aquele que possui o ângulo reto entre cateto oposto e adjacente
portanto, o sistema calcula o valor necessário da hipotenusa p manter o ângulo reto
# dois pontos flutuante após o ponto :.2f'''
