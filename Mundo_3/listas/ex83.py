print('Validando expressões matemáticas!')

expressao = (str(input('Digite sua expressão: ')))

aberto = expressao.count('(')
fechado = expressao.count(')')

if aberto == fechado:
    print('Expressão válida.')
else:
    print('Expressão inválida.')
