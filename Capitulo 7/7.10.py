ferias = {}
active = True


while active:
    name = input('Qual seu nome? ').title()
    question = input('Se pudesse viajar, iria pra onde? ').title()
    ferias[name] = question
    continuar = input('Deseja cadastrar mais pessoas? [[Y/N]').strip().upper()
    
    if continuar == 'N':
        active = False
        print('Stopping PROGRAM!')

print(ferias)

for name , place in ferias.items():
    print(f'{name} quer viajar para {place}')
