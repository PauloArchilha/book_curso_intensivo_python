favorite_numbers = {'paulo': [23, 30], 'mari': [13, 22],
                    'menor': [22, 24], 'artur': [22, 11]
                    }

for people, nums in favorite_numbers.items():
    print(f"\n{people.title()}'s favorite numbers is:", end=' ')
    for num in nums:
        print(f'{num}',end=', ')
