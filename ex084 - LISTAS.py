#Estudando Listas/São mutáveis
num = [2, 3, 6, 9, 13]
num [3] = 7 #Alterar um item
num.append(7) #Adicionar um item substituindo
num.sort(reverse=True) #Colocando em ordem decrescente
num.sort() #colocando em ordem crescente
num.insert(2, 0) #Insere um valor sem substituir
num.pop(2) #remove um item da lista
print(num)
print(f'Esta lista tem {len(num)} elementos.')

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
#valores.append(8)
#valores.append(7)
#valores.append(4)
#valores.append(13)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Chueguei ao final da lista.')
