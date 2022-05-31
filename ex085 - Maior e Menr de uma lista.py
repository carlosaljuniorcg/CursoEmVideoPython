#Saber qual é o maior e o menor na lista
mai = 0
min = 0
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if cont == 0:
        mai = min = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < min:
            min = valores[cont]
print('='*30)
print(f'O valores desta lista são {valores}.')
#print(f'O maior valor foi {max(valores)} nas posiç!oes ')
#print(f'O menor valor foi {min(valores)} nas posiç!oes ')
print(f'O maior valor digitado foi {mai} na(s) posições ', end=' ')
for i, v in enumerate(valores):
    if v == mai:
        print(f' {i}... ', end=' ')
print()
print(f'O menor valor digitado foi {min} na(s) posições ', end=' ')
for i, v in enumerate(valores):
    if v == min:
        print(f' {i}... ', end=' ')
print()



