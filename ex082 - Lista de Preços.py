#Lista de preços com tuplas
print("-"*42)
print(f'{"TABELA DE PREÇOS":^41}')
print("-"*42)
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderon', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=" ")
    else:
        print(f'R${listagem[pos]:>9.2f}')
print('-'*42)