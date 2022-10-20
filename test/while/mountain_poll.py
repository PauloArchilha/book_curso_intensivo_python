responses = {}

polling_active = True # Define uma flag para indicar que a enquete está ativa

while polling_active:
    name = input('Whats your name? ').title()
    response = input('Which mountain would you like to climb someday? ').title()
    responses[name] = response # Armazena a resposta no dicionário
    repeat = input('Would you like to let another person respond? [Y/N] ').upper().strip()[0]
    print(responses)  
    if repeat == 'N':
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f'{name} would like to climb {response}')
