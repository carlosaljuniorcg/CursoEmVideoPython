#Calculando medidas de uma parede
l = float(input('Digite a largura da parede: '))
a = float(input('Digite da altura da parede: '))
d = l * a 
print(('Sua parede tem dimensão de {} x {} e sua área é de {:.3f} m2. Para pintar essa parede, você precisará de {:.3f}l de tinta.').format(l, a, d, (d/2)))