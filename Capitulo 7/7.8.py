sandwich_orders = ['hamburguer', 'pastrami',
                   'hot-dog', 'mortadela', 'presunto', ]
finished_sandwiches = []


while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwiches)
print('Os lanches que você pediu foi: ', end='')
for sandwiches in finished_sandwiches:
    print(sandwiches.title(), end=', ')
