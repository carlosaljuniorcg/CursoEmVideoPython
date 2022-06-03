#Estudo sobre dicionário
pessoas = {'nome': 'Carlos', 'sexo': 'M', 'idade': '41'}#Dicionários sempre usam {}
pessoas['peso'] = 98.5#Forma de adicionar um item ao dicionario
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())#Saber as chaves Ex. nome
print(pessoas.values())#SAber os componenetes das chaves Ex. Carlos
print(pessoas.items())#Saber as chaves e os componentes
for k in pessoas.keys():#Saber as chaves formatadas
    print(k)
for k in pessoas.values():#Saber os componentes formatados
    print(k)
for k, v in pessoas.items():#Saber chaves e componenetes formatados
    print(f'{k} = {v}')

#Criando uma lisra apartir de dicionários
brasil = []
estado1 = {'uf': 'Campina Grande', 'sigla': 'PB'}
estado2 = {'uf': 'Caruaru', 'sigla': 'PE'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)