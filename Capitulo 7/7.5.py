idade = ''
active = True

while active:
    idade = input('Digite a idade! [quit to exit]: ')
    if idade == 'quit':
        idade = str(idade)
        active = False
        print('PARANDO PROGRAMA!')
    else:
        idade = int(idade)
        if idade <= 3:
            print('Não paga entrada!')
        elif idade <= 12:
            print('Ingresso custa $10.0 ')
        else:
            print('Ingresso custa $15.0 ')
