#Criando um sistema de modulazição
from tempfile import tempdir


def Linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt)
    