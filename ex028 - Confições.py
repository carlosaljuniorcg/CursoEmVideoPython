"""Jtempo = int(input('Quantos anos tem seu carro?'))
#print('carro novo' if tempo <=3 else 'carro velho')
if tempo <=3:
    print('Carro novo!')
else:
    print('Carro experiente! rsrs')
print('---FIM---')"""

#nome = str(input('Qual é seu nome? '))
#if nome == 'Carlos':
#    print('Que nome mais lindo! Combina contigo. =)')
#else: 
#    print('Seu nome é tão normal!')
#print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2
print('Sua média é {:.1f}.'.format(media))
#print('Parabéns!! if >= 6 else'Estude mais!')
if media >= 6.0:
    print('Parabéns! Você foi aprovado.')
else:
    print('Lamento! Reprovado. Estude mais um pouco!')
