#Valores únicos em uma lista
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('='*40)
numeros.sort()
print(f'Você digitou os valores de {numeros}.')