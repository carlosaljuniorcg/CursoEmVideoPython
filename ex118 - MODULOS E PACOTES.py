#from uteis import fatorial, dobro #Módulo personalizado
import uteis

num = int(input('Digite o valor: '))
fat = uteis.fatorial(num)#Usando um mú
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {uteis.dobro(num)}.')
print(f'O triplo de {num} é {uteis.triplo(num)}.')
print(f'A potência quadrada de {num} é {uteis.potencia2(num)}.')
print(f'A potência cúbica de {num} é {uteis.potencia3(num)}.')
