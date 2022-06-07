from time import sleep

def maior(* num):
    cont = maior = 0
    print('-'*30)
    print('Analisando os blocos passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informafo foi {maior}.')


#Função principal
maior(10, 21, 3, 7, 2, 44)
maior(4, 7, 8, 3, 2)
maior(1, 2)
maior(0)
maior()