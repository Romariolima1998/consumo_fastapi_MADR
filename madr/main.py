import os
from madr.request import make_request

token = False
url_login = 'http://127.0.0.1:8000/auth/token'
url_users = 'http://127.0.0.1:8000/users'
url_romancista = 'http://127.0.0.1:8000/romancista'
url_livro = 'http://127.0.0.1:8000/livros'


def login(url, data):

    request = make_request(
        'post', url, data=data)

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

    if request.status_code != 201:
        print(response.get('detail'))
        return

    print('usuario criado com sucesso \n')
    print(f'id: {response["id"]}')
    print(f'username: {response["username"]}')
    print(f'email: {response["email"]}')


def list_users(url, index):
    url = url + f'?offset={index}'

    request = make_request('get', url)

    response = request.json()

    if request.status_code != 200:
        print(response.get('detail'))
        return

    return response


def update_user(url, id, data, headers):
    url = url + f'/{id}'
    request = make_request('put', url, json=data, headers=headers)

    response = request.json()

    if request.status_code != 200:
        print(response.get('detail'))
        return

    print(f'id: {response["id"]}')
    print(f'username: {response["username"]}')
    print(f'email: {response["email"]}')


def delete(url, id, headers):
    url = url + f'/{id}'

    request = make_request('delete', url, headers=headers)

    response = request.json()

    if request.status_code != 200:
        print(response.get('detail'))

    print(response['message'])


def search(url, nome):
    url = url + f'?nome={nome}'

    request = make_request('get', url)

    response = request.json()

    if request.status_code != 200:
        print(response.get('detail'))
        return

    return response


def create(url, data, headers):
    request = make_request(
        'post', url, json=data, headers=headers)

    response = request.json()

    if request.status_code != 201:
        print(response.get('detail'))
        return

    print('criado com sucesso \n')

    return response


def update(url, id, data, headers):
    url = url + f'/{id}'
    request = make_request('patch', url, json=data, headers=headers)

    response = request.json()

    if request.status_code != 200:
        print(response.get('detail'))
        return
    print('atualizado com sucesso \n')

    return response


# ----------------------------------------------------------------------------
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
            user = input('digite seu usuario: ')
            password = input('digite sua senha: ')

            data = {"username": user, "password": password}

            token = login(url_login, data)
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

# ---------------------------------------------------------------------------------------

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
                    index = 0
                    while True:
                        users = list_users(url_users, index)
                        for key, value in users.items():
                            for user in value:
                                print(
                                    '######################################################### \n')
                                print(f'id: {user["id"]}')
                                print(f'username: {user["username"]}')
                                print(f'email: {user["email"]}')
                        print(
                            '#############################################################')
                        print('digite: s, para sair, ou qualquer tecla para proximo')

                        value = input('digite a opcao desejada: ')
                        if value.lower() == 's':
                            break

                        index += 1

                elif value == '2':
                    try:
                        id = int(
                            input('digite o id do usuario que deseja atualizar: '))
                    except:
                        print('digite apenas numeros')
                        continue

                    username = input('digite o username: ')
                    email = input('digite seu email: ')
                    password = input('digite a senha: ')

                    data = {
                        "username": username,
                        "email": email,
                        "password": password
                    }

                    headers = {"Authorization": token}

                    update_user(url_users, id, data, headers)

                elif value == '3':
                    try:
                        id = int(
                            input('digite o id do usuario que deseja deletar: '))
                    except:
                        print('o id deve ser um numero')

                    headers = {"Authorization": token}

                    delete(url_users, id, headers)

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
                    nome = input(
                        'digite o nome do romancista que deseja procurar: ')

                    romancistas = search(url_romancista, nome)

                    for key, value in romancistas.items():
                        for romancista in value:
                            print(
                                '######################################################### \n')
                            print(f'id: {romancista["id"]}')
                            print(f'nome: {romancista["nome"]}')

                elif value == '2':
                    nome = input('digite o nome do romancista: ')
                    data = {
                        "nome": nome
                    }
                    headers = {"Authorization": token}

                    romancista = create(url_romancista, data, headers)

                    if romancista:
                        print(f'id: {romancista["id"]}')
                        print(f'nome: {romancista["nome"]}')

                elif value == '3':
                    try:
                        id = int(input(
                            'digite o id do romancista que deseja atualizar: '))
                    except:
                        print('o id deve ser um numero')
                        continue

                    nome = input('digite o novo nome do romancista: ')
                    data = {
                        "nome": nome
                    }
                    headers = {"Authorization": token}
                    romancista = update(url_romancista, id, data, headers)

                    if romancista:
                        print(f'id: {romancista["id"]}')
                        print(f'nome: {romancista["nome"]}')

                elif value == '4':
                    try:
                        id = int(input(
                            'digite o id do romancista que deseja deletar: '))
                    except:
                        print('o id deve ser um numero')
                        continue

                    headers = {"Authorization": token}

                    delete(url_romancista, id, headers)

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
