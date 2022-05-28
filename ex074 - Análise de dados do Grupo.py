tot18 = totH = totM20 = 0
while True:
    idade = int(input('Qual sua Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quar continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f"Total de pessoas com mais de 18 anos: {tot18}")
print(f'Ao todo tamos um total de {totH} homens cadastrados.')
print(f'Total de mulher com menos de 20 anos é {totM20}.')
print('E por hoje é só pessoal.')
