ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numbers in ordinal_numbers:
    if numbers == 1:
        print(f'{numbers}st')
    elif numbers == 2:
        print(f'{numbers}nd')
    elif numbers == 3:
        print(f'{numbers}rd')
    else:
        print(f'{numbers}th')
