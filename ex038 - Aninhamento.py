#Estruturas aninhadas
nome = str(input('Qual é seu nome: '))
if nome == 'Carlos':
    print('Que belo nome. Combina com você!')
elif nome == 'Pedro' or nome == 'Stella' or nome == 'Anderson':
    print('Seu nome é bem comum.')
elif nome in 'Ana, Karla, Rísia, Stella':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))