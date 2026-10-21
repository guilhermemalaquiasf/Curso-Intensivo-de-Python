pizzas_minhas = ['marinara', 'quatro queijos', 'palmito', 'napolitana']
pizzas_amigos = pizzas_minhas[:]

pizzas_minhas.append('cinco queijos')
pizzas_amigos.append('gorgonzola')

print('Minhas pizzas favoritas são: ')
for pizza in pizzas_minhas:
    print(pizza.title())

print('\nAs pizzas favoritas do meu amigo são: ')
for pizza in pizzas_amigos:
    print(pizza.title())


print("Este " + "é um teste")