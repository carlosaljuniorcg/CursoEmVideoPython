
while True:
    num = int(input('Quer ver a tabuada de que valor? '))
    if num < 0:
            break
    print ('-'*20)
    for c in range(1, 10):
        print(f'{num} x {c:2} = {num*c:2}')
    print ('-'*20)
print('Programa de Taboada finalizado. =)')