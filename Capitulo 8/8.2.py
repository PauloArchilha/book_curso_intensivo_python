def favorite_book(book):
    print(f'Your favorite book is: {book}')
   
   
book = input('What is your favorite book? ')
favorite_book(book.title())


livro = input('Outro livro: ')
favorite_book(livro)
