sandwich_orders = ['hamburguer', 'pastrami',
                   'hot-dog', 'mortadela', 'pastrami', 'presunto', 'pastrami' ]
finished_sandwiches = []
print('Estamos sem lanche de pastrami hoje. Desculpe!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwiches)
print('Hoje temos apenas: ',end='')
for sandwich in finished_sandwiches:
    print(f' {sandwich}',end=', ')

