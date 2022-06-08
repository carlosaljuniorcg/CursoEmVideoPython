C = ('\033[m', 
     '\033[0;30;41m'
);


def ajuda(com):
    help(com)

def título (msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
    print(c[0], end='')

#Programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PY HELP', 1)
    comando = str(input('Função ou Biblioteca > ')).upper()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)