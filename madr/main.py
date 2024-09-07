import os

token = False


if not token:
    while True:
        
        print('''
    digite: 1 para fazer login,
    digite: 2 para criar usuario
    digite: s para sair
                ''')
        
        value = input('digite a opcao desejada: ')
        os.system('clear')

        if value == '1':
            ...
        elif value == '2':
            ...
        elif value.lower() == 's':
            break

        else:
            print(' opcao invalida') 

if token:
    while True:
        os.system('clear')



