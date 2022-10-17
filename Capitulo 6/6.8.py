tico = {'tipo': 'cachorro', 'dono': 'paulo'}
luna = {'tipo': 'cachorro', 'dono': 'mari'}
neguinha = {'tipo': 'gato', 'dono': 'paulo'}
pets = [tico, luna, neguinha]


for pet in pets:
    print(f'O tipo: {pet["tipo"]} e o dono: {pet["dono"].title()}')
