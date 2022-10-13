list_names = []

if list_names:
    for name in list_names:
        if name == 'admin':
            print(f'Bom dia {name}')
        else:
            print(f'Ola {name}, obrigado por logar novamente!')
else:
    print('Quer cadastrar um novo usuário?')
