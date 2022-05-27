from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 7:
    print('''    1. somar
    2. multiplicar
    3. maior
    4. novos números
    5. dividir
    6. Potência
    7. sair do programa
    Qual é a sua opção?''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação de {} x {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        div = n1 / n2
        print('O resultado desse dividão entre {} e {} é {}'.format(n1, n2, div))
    elif opcao == 6:
        pot = n1 ** n2
        print('A potência de {} e {} é {}'.format(n1, n2, pot))
    elif opcao == 7:
        print('FInalizando...')
    else:
        print( 'Opção inválida. Tente novamente.')
    print('=-='*10)
    sleep(2)
print('Fom do programa. Volte sempre!')