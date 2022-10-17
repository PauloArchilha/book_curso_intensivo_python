people_1 = {'first': 'Paulo', 'last': 'Archilha',
            'age': 31, 'city': 'Severinia'}
people_2 = {'first': 'Mari', 'last': 'Pereira',
            'age': 22, 'city': 'Severinia'}
people_3 = {'first': 'Artur', 'last': 'Haines',
            'age': 29, 'city': 'SP'}

peoples = [people_1, people_2, people_3]

for people in peoples:
    full_name = people['first'] + ' ' + people['last']
    print(f'Nome completo: {full_name} , idade: {people["age"]}, cidade: {people["city"]}.')

