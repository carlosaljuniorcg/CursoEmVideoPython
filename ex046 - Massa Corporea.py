#Calcular IMC
peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura**2)
print('Seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso.')
elif 18.5 <= imc < 24.9:
    print('Parabéns!!! Você está com PESO IDEAL.')
elif 24.9 <= imc < 29.9:
    print('Você está com SOBREPESO.')
elif 29.9 <= imc < 39.9:
    print('CUIDADO! Você está OBESO.')
else:
    print('Procure um especilista. Você está com OBESIDADE MÓRBIDA.')


