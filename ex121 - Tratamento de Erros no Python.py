try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é poss~ivel dividir o número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else: 
    print(f'O resultado é {r}.')
finally:
    print('Volte sempre!!! Muito obrigado.')