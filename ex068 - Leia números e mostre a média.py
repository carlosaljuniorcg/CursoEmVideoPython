#Leia números inteiros e mostre suas médias
resp = 'S'
soma = quant = media = maior = menor = 0
while resp == 'S':
    num = int(input('Digite um número inteiro: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Você dgitou {quant} e a média desses números é {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')
