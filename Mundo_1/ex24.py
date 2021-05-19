cidade = (input('Em que cidade você nasceu?: ')).strip()
print('Santo é a primeira palavra da sua cidade? {}'.format(cidade[:5].lower() == 'santo'))
