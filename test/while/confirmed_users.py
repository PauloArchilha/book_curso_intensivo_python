# Começa comos usuários que precisam ser verificados, 
# e com uma lista vazia para armazenar os usuários confirmados


unconfirmed_users = ['alice','brian', 'candace']
confirmed_users = []

# Verifica cada usuário até que não haja mais usuários não confirmados
#Transfere cada usuário verificado para a lista de usuários confirmados

while unconfirmed_users:
    current_user = unconfirmed_users.pop() # a função pop() remove os usuários da lista de não verificados
    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user) # 
print(f'{unconfirmed_users}') # Lista tem que estar vazia
    
print('The following users have been confirmed: ') # Exibe todos os usuários confirmados
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

