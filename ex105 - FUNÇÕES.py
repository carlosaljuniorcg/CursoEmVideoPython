#Aula sobre função
#Definindo linhas com comando print
print('-=' * 30)
print('    CURSO EM PYTHON    ')
print('-=' * 30)
#Usando a função DEF para criar uma rotina
def lin():
    print('-='*30)
#Programa principal
lin()
print('    CURSO EM PYTHON    ')
lin()

def titulo(txt):
    print('-='*30)
    print(txt)
    print('-='*30)

titulo('    CURSO EM VIDEO    ')
titulo('    CARLOS CURSINHO    ')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    #print(s)
    
soma(33, 4)
soma(3, 6)
soma(10, 12)
soma(b=15, a=20)

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao lado {tam} números.')
    
contador(2, 1, 3)
contador(12, 9, 13)
contador(1, 6, 7, 8, 9)

def dobra (list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

valores = [13, 14, 2, 25, 1]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')

soma(7, 3)
soma(10, 6, 21)
soma(6, 5)
