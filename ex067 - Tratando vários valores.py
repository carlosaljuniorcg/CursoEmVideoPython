#Tratando vários números
num = cont = soma = 0
num = int(input('Digite um número [Digite 999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [Digite 999 para parar]: '))       
print(f'Você digitou {cont} e a soma desses números é {soma}.')