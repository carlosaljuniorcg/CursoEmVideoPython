#Mais de funções...


from calendar import c


def teste():
    x = 8#escopo ou variável local por está dentro de um conjunto
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')

#Programa principal
n = 2#Escopo ou variável global por está fora de um conjunto
print(f'No programa principal, n vale {n}.')
#print(f'No programa principal, x vale {x}.')

def funcao():
    n1 = 4#N1 dentro é um escopo local
    print(f'N1 dentro vale {n1}.')

n1 = 2#N1 fora é um escopo glocal
funcao()
print(f'N1 fora vale {n1}.')


def somar(a=0, b=0, c=0):
    s = a + b + c
    #print(f'A soma vale {s}.')
    return s

r1 = somar(3, 2, 2)
r2 = somar(2, 4)
r3 = somar(3)
print(f'Meus cálculos valem {r1}, {r2} e {r3}.')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')