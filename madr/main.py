import os

token = True


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
            print('opcao invalida')

if token:
    while True:
        print(
            '''
    digite: 1 para usuario.
    digite: 2 para romancista.
    digite: 3 para livros
    digite: s para sair.
'''
        )

        value = input('digite a opcao desejada: ')
        os.system('clear')
#############################################
        if value == '1':
            while True:
                print(
                    '''
    digite: 1 para listar
    digite: 2 para atualizar.
    digite: 3 para deletar.
    digite: s para voltar.
'''
                )
                value = input('digite a opcao desejada: ')
                os.system('clear')

                if value == '1':
                    ...
                elif value == '2':
                    ...
                elif value == '3':
                    ...
                elif value.lower() == 's':
                    break

                else:
                    print('opcao invalida')
    ###############################################################

        elif value == '2':
            while True:
                print(
                    '''
        digite: 1 para pesquisar por romancista.
        digite: 2 para criar romancista.
        digite: 3 para atualizar um romancista.
        digite: 4 para deletar romancista.
        digite: s para voltar.
    '''
                )

                value = input('digite a opcao desejada: ')
                os.system('clear')

                if value == '1':
                    ...
                elif value == '2':
                    ...
                elif value == '3':
                    ...
                elif value == '4':
                    ...
                elif value.lower() == 's':
                    break

                else:
                    print('opcao invalida')


#############################################################################

        elif value == '3':
            while True:
                print(
                    '''
        digite: 1 para pesquisar por livro.
        digite: 2 para criar livro.
        digite: 3 para atualizar um livro.
        digite: 4 para deletar livro.
        digite: s para voltar.
    '''
                )

                value = input('digite a opcao desejada: ')
                os.system('clear')

                if value == '1':
                    ...
                elif value == '2':
                    ...
                elif value == '3':
                    ...
                elif value == '4':
                    ...
                elif value.lower() == 's':
                    break

                else:
                    print('opcao invalida')

        elif value.lower() == 's':
            break

        else:
            print('opcao invalida')
