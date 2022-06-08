#Usando módulo da mesma pasta
import moedas

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${moedas.metade(p)}')
print(f'O dobro de R${p} é R${moedas.dobro(p)}')
print(f'Com o aumento de 10% temos {moedas.aumentar(p, 10)}')