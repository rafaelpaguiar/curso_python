users = []
users = ['admin', 'user1', 'user2', 'user3', 'user4',]

if users:
    for user in users:
        if user == 'admin':
            print(f"Olá {user}, gostaria de ver um relatório?")
        else:
            print(f"Olá {user}, obrigado por fazer login novamente.")
else:
    print("É necessário encontrar alguns usuários")