#Aumentos multiplos
salario = float(input('Informe seu salário: '))
if salario >= 1250:
    total = salario + (salario * (10/100))
if salario < 1250:
    total = salario + (salario * (15/100))
print("Seu salário com aumento é R$ {:.2f}.".format(total))