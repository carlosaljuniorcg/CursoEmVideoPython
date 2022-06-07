def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m2.')


#Programa principal
print('<<CONTROLE DE TERRENOS>>')
print('-'*20)
l = float(input('LARGURA (M): '))
c = float(input('COMPRIMENTO (M): '))
area(l, c)