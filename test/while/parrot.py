prompt = '''Tell me something, and I will repeat it back to you:
\nEnter 'quit' to end the program. '''
message = ''

while message != 'quit':
    message = input(prompt ).strip().lower()
    if message != 'quit':
        print(message)
   
    