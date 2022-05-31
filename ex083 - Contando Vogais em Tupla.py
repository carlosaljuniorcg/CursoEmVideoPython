#Contando voagais em tuplas
palavras = ('Cachorro', 'Programador', "Python", 'Resenha', 'Carlos', 'Risia', 'Amor', 'Pai', 'Filha', 'Vila', 'Disco', 'Trilha', 'Bicicleta', 'Moto', 'Carro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')