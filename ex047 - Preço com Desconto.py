#Calcular valor com ou sem desconto
print('{:=^40}'.format('LOJAS CARLOS ANTÔNIO'))

valor = float(input('Digite o valor: '))
print('O valor de sua compra é de R${:.2f}.'.format(valor))
print('''FORMA DE PAGAMENTO:
1. À vista dinheiro/débito/PIX: 10% de desconto
2. À vista no cartão: 5% de desconto
3. Em até 2x no cartão: Preço normal
4. 3x ou mais no cartão: 20% de juros''')
opcao = int(input('Qual sua opção? '))
if opcao == 1:
    print('O valor da compra com desconto de 10% é de R${:.2f}.'.format(valor-(valor*10/100)))
elif opcao == 2:
    print('O valor da sua compra com desconto de 5% é de R${:.2f}.'.format(valor-(valor*5/100)))
elif opcao == 3:
    total = valor
    parcela = total / 2
    print('Sua compra parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
    print('Seu compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
elif opcao == 4:
    total = valor+(valor*20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua comprar será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
    print('Sua com de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))

else:
    print('Opção inválida. Tente novamente.')



