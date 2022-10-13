favorite_languages = {
'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', 'paulo': 'python', 'mari': 'javascript' }
new_peoples = ['artur', 'menor', 'bruna', 'tairine', 'paulo', 'mari']

for people in new_peoples:
    if people in favorite_languages:
        print(f'Você já participou, {people.title()}')
    else:
        print(f'Obrigado por terem participado! {people.title()}')
