favorite_places = {'paulo': ['casa','quarto', 'praia'],
                   'mari': ['cozinha', 'restaurante'],
                   'menor': ['rio preto', 'apartamento']}


for peoples , places in favorite_places.items():
    print(f'\n{peoples.title()}',end=' ')
    for place in places:
        print(f'{place}',end=', ')

