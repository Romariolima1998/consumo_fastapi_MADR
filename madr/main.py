import os
from madr.request import make_request

token = False
url_login = 'http://127.0.0.1:8000/auth/token'
url_users = 'http://127.0.0.1:8000/users'


def login(url):

    user = input('digite seu usuario: ')
    password = input('digite sua senha: ')

    request = make_request(
        'post', url, data={"username": user, "password": password})

    response = request.json()

    if request.status_code != 200:
        print(response.get('detail'))
        return

    print('logado com sucesso')

    return f'{response.get("token_type")} {response.get("access_token")}'


def create_user(method, url, data):

    request = make_request(
        method, url, json=data)

    response = request.json()

    if request.status_code != 200:
        print(response.get('detail'))
        return

    print('usuario criado com sucesso')


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
            token = login(url_login)
            if token:
                break

        elif value == '2':
            username = input('digite um username: ')
            email = input('digite seu email: ')
            password = input('digite uma senha: ')

            data = {
                "username": username,
                "email": email,
                "password": password
            }
            create_user('post', url_users, data)

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
