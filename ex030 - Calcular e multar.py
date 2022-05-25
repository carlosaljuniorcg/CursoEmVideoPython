#Criar programa para multar carro
p1 = int(input('Digite qual é sua velocidade: '))
if p1 >= 50:
    m = (p1 - 50)*7
    print('Você foi multado! E sua multa é no valor de R$ {}.'.format(m))
else:
    print('Muito bem! Tenha um bom dia!')
