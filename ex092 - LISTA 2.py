teste = list()
teste.append('Carlos')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Antônio'
teste[1] = 41
galera.append(teste[:])
print(galera)   

pessoas = [['Carlos', 40], ['Risia', 45], ['Keylla', 22], ['Pedro', 11]]
print(pessoas[3][0])#Ele vai printar apenas o item 0 da lista 3
for p in pessoas:#Ele vai printar apenas os nomes
   # print(p[0])
    print(f'{p[0]} tem {p[1]} anos.')

gente = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    gente.append(dados[:])
    dados.clear()

print(gente)

for p in gente:
    if p[1] >= 23:
        print(f'{p[0]} é maior de idade.')
    elif p[1] <= 22:
        print(f'{p[0]} é menor de idade.')
