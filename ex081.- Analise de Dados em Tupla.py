#Analise de dados em uma tupla
dados = (int(input('Digite um número: ')), 
int(input('Digite outo número: ')), 
int(input('Digite mais um número: ')), 
int(input('Digite mais um último número: ')))

print(f'Você digitou os valores: {dados}')
print(f'O valor 9 apareceu {dados.count(9)} vezes')
if 3 in dados: 
    print(f'O valor 3 aparece na posição {dados.index(3)+1}.')
else:
    print('O valor 3 não foi digitado em nenhuma posiçào.')
print(f'A quantidade de números pares foi ', end=' ')
for n in dados:
    if n % 2 == 0:
        print(n, end=' ')


