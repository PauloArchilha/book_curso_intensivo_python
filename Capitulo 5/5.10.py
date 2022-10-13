current_users = ['paulo', 'mari', 'menor', 'artur', 'admin']
new_users = ['bruna', 'tairine', 'artur', 'MARI', 'lucas']


for user in new_users:
    if user.lower() in current_users:
        print(f'Nome: {user.title()} já cadastrado')
    else:
        print(f'Nome: {user.title()} cadastrado com sucesso!')
