
pessoas = []
temp = []
mai = men = 0
while True:
    pessoas.append(str(input('Digite seu nome: ')))
    pessoas.append(float(input('Digite seu peso: ')))
    if len(temp) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    temp.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(temp)} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de', end=" ")
for p in temp:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men}kg. Peso de', end=" ")
for p in temp:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
print()

