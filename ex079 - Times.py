times = ('Palmeiras', 'Atlético - MG', 'Corinthias', 'Coritiba', 'São Paulo', 'Atlético-PR', 'Botafogo', 'Flamengo', 'Santos', 'América-MG', 'Fluminense', 'Avai', 'Gragantino', 'Internacional', 'Goias', 'Cuiabá', 'Juventude', 'Ceará-SC', 'Atlético-GO', 'Fortaleza')
#timealf = (sorted(times))
#Juventude = (times.index('Juventude'))  
print(f'Os cinco primeiros times da tabela são: {times[0:5]}')
print('-='*63)
print(f'Os quatro últimos colocados sào: {times[-4:]}')
print('-='*63)
print(f'Os times em ordem alfabéticas são: {sorted(times)}.')#Uso de colchetes e parenteses
print('-='*63)
print(f'O Juventude está na posiçào {times.index("Juventude")+1}.')# Aspas duplas fazem a interpolação