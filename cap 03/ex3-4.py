convidados = ['joão', 'maria', 'tereza']
print('Você está convidado, querido ', convidados[0].title())
print('Você está convidada, querida ', convidados[1].title())
print('Você está convidada, amiga ', convidados[2].title())

print('João não poderá comparecer\n\n')

convidados[0] = 'felipe'
print('Você está convidado, querido ', convidados[0].title())
print('Você está convidada, querida ', convidados[1].title())
print('Você está convidada, amiga ', convidados[2].title())

print('\n\n\n Encontrei uma mesa maior')
convidados.insert(3, 'selena')
convidados.insert(4, 'luiza')
convidados.append('pedro')

print('Você está convidado, querido ', convidados[0].title())
print('Você está convidada, querida ', convidados[1].title())
print('Você está convidada, amiga ', convidados[2].title())
print('Você está convidado, querido ', convidados[3].title())
print('Você está convidada, querida ', convidados[4].title())
print('Você está convidada, amiga ', convidados[5].title())

print('\n\n Agora só posso convidar duas pessoas para o jantar.')
print('Lamento por ter que não poder te convidar para o jantar, ', convidados.pop().title())
print('Lamento por ter que não poder te convidar para o jantar, ', convidados.pop().title())
print('Lamento por ter que não poder te convidar para o jantar, ', convidados.pop().title())
print('Lamento por ter que não poder te convidar para o jantar, ', convidados.pop().title())

print('\n\n', convidados[0].title(), ' e ', convidados[1].title(), ', vocês estão convidados')
del convidados[1]
del convidados[0]
print(convidados)