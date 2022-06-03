#Palpites para números da Megasena
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 29)
print('                     JOGA NA MEGA SENA                  ')
print('-=' * 29)
quant = int(input('Quantos jogos você deseja fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 10, f'SORTEANDO {quant} JOGOS', '-=' * 10)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='* 11, '< BOA SORTE >', '-='*11)
