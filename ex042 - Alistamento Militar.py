#Analisar alistamento militar
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para se alistar.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade == 18:
    print('Seu tempo de alistamento chegou!')
else:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento deveria ter sido em {}.'.format(ano))
    