#COnversor de moedas
real = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Você pode comprar US${:.2f}.'.format(real/4.93))

bit = float(input('Quanto você 2em em bitcoins? '))
print('Você tem {} bitcoins que correspondem a R${:.4f}.'.format(bit, bit*148.662))