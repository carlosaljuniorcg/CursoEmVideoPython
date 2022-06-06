#Aprimorando a lista de Jogadores do exercicico anterior.
time = list()
jogador = dict()
partidas = list()
while True: 
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas com S ou N.')
    if resp == 'N':
        break
print('-'*30)
print('cod ', end='') #Esse código é para fazer o cabeçalho
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time): 
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (Para parar digite 999) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print('     No jogo {i} fez {g} gols. ')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
