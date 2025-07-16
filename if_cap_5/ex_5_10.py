current_users = ['user1','user2','User3','user4','user5']
new_users = ['user3','user5','user6','user7','user8']

for new_user in new_users:
    current_users_normalized = [user.lower() for user in current_users]
    if new_user in current_users_normalized:
        print('Usário já existe!')
    else:
        print('Nome de usuário disponível.')