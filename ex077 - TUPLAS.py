lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim' #Tuplas são imutáveis
#print(Lanche[:2])
print(sorted(lanche))
print(lanche.count('Suco')) #Conta quantas vezes tem o objeto na tupla
print(lanche.index('Suco')) #Indica qual a posição do item na tupla

for cont in range(0, len(lanche)):
   print(f'Eu vou comer{lanche[cont]} na posição {cont}')

#print(len(lanche))
for comida in lanche:
    print(f'Eu vou comar {comida}')
print('Comi pra caramba!') 