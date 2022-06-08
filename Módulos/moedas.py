def aumentar(p = 0, t = 0, formato=False):
    """
    -> Calcula o aumento de um determinado preço, 
    retornando o resultado com o sem formtação.
    :param p: O preço que se quer reajustar.
    :param t: Qual é a procetagem do aumento.
    :return: O valor reajustado com ou sem formato.
    """
    res = p + (p*t/100)
    return res if formato is False else moedas(res)

    
def diminuir(p = 0, t = 0, formato=False):
    res = p - (p*t/100)
    return res if formato is False else moedas(res)

  
def dobro (p = 0, formato=False):
    res = p * 2
    return res if not formato else moedas(res)

    
def metade(p = 0, formato=False):
    res = p / 2
    return res if not formato else moedas(res)

def moedas(p = 0, moedas = 'R$'):
    return f'{moedas}{p:>.2f}'.replace('.', ',')

def resumo(p=0, taxaa=10, taxar=5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analizado: \t{moedas(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metado do preço: \t{metade(p, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(p, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(p, taxar, True)}')
    print('-'*40)