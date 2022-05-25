#Pegar o ano do atleta e mostrar sua modalidade
from datetime import date
atual = date.today().year
ano = int(input('Informe o ano de seu nascimento: '))
data = atual - ano
print('Você nasceu no ano de {} e tem {} anos.'.format(ano, data))
if data <= 9:
    print('Você está na modalidade MIRIM.')
elif data <= 14:
    print('Você estã na modalidade INFANTIL.')
elif data <= 19:
    print('Você está na modalidade JÚNIOR.')
elif data <= 25:
    print('Você está na modalidade SÊNIOR.')
else:
    print('Você está na modalidade MASTER.')
