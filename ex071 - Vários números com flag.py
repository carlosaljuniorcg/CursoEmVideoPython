num = soma = cont = 0
while True:
    num = int(input('Digite um número [Digite 999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A quantidade de valores digitados foi {cont}.')
print(f'E a soma desses valores é {soma}')
print('FIM')

