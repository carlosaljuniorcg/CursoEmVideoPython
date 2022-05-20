#Leia uma numero inteiro e mostre na tela o seu sucessor e antecessor
n = int(input('Digite um número: '))
#a = n - 1 
#s = n + 1
print('Analisando o seu valor {}, temos seu antecessor {} e seu sucessor {}.'. format(n, (n-1), (n+1)))

#Dobro, triplo e raiz quadrada

n = int(input('Digite um valor: '))
print('O valor é {}, o dobro do valor é {} e a sua raiz quadrada é {:.2f}'.format(n, (n*2), (n**(1/2))))