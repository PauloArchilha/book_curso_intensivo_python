active = True

while active:
    message = input('Você quer continuar? ')
    if message == 'quit':
        active = False
        print('PARANDO!')
    else:
        print('Vamos continuar sim!')
