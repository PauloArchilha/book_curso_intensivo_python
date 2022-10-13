rivers = {'river nile': 'egito', 'river amazonas': 'brazil', 'river danube': 'europe' }

for river, country in rivers.items():
    print(f'{river.title()} is part of {country.title()}')


for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
