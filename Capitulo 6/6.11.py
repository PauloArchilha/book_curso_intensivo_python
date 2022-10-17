cities = {'severinia': {'country': 'brazil', 'population': '20.000', 'fact': 'minuscula'},
          'rio preto': {'country': 'brazil', 'population': '500.000', 'fact': 'big'},
          'olimpia': {'country': 'brazil', 'population': '70.000', 'fact': 'best place',},}

for city , cities_info in cities.items():
    
    country_info = cities_info['country'].title()
    popu_info = cities_info['population'].title()
    fact_info = cities_info['fact'].title()
    print(f'{city.title()}: {country_info}, {popu_info}hbts, {fact_info} ')
    """_summary_
    """
