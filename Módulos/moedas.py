def aumentar(p = 0, t = 0, formato=False):
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