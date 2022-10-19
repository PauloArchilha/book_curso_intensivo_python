pizza = ''

while True:
    pizza = input('Digite os ingredientes: ').strip().lower()
    if pizza == 'quit':
        break
    print(f'Adicionado: {pizza.title()}')
print('Obrigado por fazer o pedido!')
