current_users = ['luis', 'pedro', 'flaviana', 'roberta', 'guilherme', 'admin']
new_users = ['luis', 'soraia', 'leticia', 'giovana', 'rafaela', 'daniela']

for user in new_users:
    if user in current_users:
        print(f"{user}, você precisa inserir um nove nome de usuário")
    else:
        print(f"O nome de usuário {user} está disponível")