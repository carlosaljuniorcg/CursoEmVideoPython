#Leia duas notas e dê a média com uma mensagem
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f} sua média final foi {:.1f}.'.format(n1, n2, media))
print(media)
if media <= 5:
    print('Você está REPROVADO')
elif 5 <= media <= 6.9:
    print('Você está em RECUPERAÇÃO')
#elif media <= 6.9:
 #   print('RECUPERAÇÃO')
elif media >= 7:
    print('Você foi APROVADO! Parabéns!!!')