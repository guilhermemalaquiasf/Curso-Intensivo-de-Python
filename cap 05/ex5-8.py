nomesUsuarios = ['luis', 'pedro', 'flaviana', 'roberta', 'guilherme', 'admin']

if nomesUsuarios:
    for nome in nomesUsuarios:
        if nome == 'admin':
            print("Olá, administrador, gostaria de ver um relatório de status?")
        else:
            print(f"{nome}, obrigado por fazer login novamente")
else:
    print("É necessário encontrar alguns usuários!")