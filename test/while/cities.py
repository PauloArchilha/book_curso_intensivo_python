

while True:
    cities = input('Please, enter the name of a city you have visited: ').strip().lower()
    if cities == 'quit':
        break
    else:
        print(f"I'd love to go to {cities.title()}")
