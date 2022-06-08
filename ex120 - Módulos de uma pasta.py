#Usando um módulo de uma pasta diferente
from Módulos import moedas 
from Módulos import dado


p = dado.leiaDinheiro('Digite o preço: R$')
#p = float(input('Digite o preço: R$'))
#print(f'A metade de {moedas.moedas(p)} é {moedas.metade(p, True)}')
#print(f'O dobro de {moedas.moedas(p)} é {moedas.dobro(p, True)}')
#print(f'Com o aumento de 10% temos {moedas.aumentar(p, 10, True)}')
#print(f'Diminuindo em 13% temos {moedas.diminuir(p, 13, True)}')
moedas.resumo(p, 20, 15)    