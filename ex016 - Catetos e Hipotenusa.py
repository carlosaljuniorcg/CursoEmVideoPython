#Calculo do cateto oposto e cateto adjacente são iguais a hipotenusa.
#import math
from math import hypot
co = float(input('Comprimeto do cateto oposto: '))
ca = float(input('Comprimeto do cateto adjacente: '))
#hi = (co**2+ca**2)**(1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))