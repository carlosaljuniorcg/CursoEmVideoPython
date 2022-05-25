from random import randint
from time import sleep
computador = randint(0, 10) #Faz o computador pensar
print('-*-' * 19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-*-' * 19)
jogador = int(input('Em que número eu pensei? ')) #O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer.')
else: 
    print('Eu pensei no número {} e não no {}. Tente novamente!'.format(computador, jogador))