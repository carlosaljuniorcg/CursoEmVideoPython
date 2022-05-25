#Calculando passando de ônibus
distancia = float(input('Quantos km você percorreu? '))
print('Sua viagem foi de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
    print('Sua viagem custou R$ {:.2f}.'.format(preco))