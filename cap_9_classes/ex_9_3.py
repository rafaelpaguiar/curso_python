class User:
    def __init__(self,user_name,first_name,last_name,email):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def describe_user(self):
        print(f"User name : {self.user_name}")
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"E-mail : {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

user1 = User("jdoe123", "John", "Doe", "jdoe@example.com")
user2 = User("msmith", "Mary", "Smith", "mary.smith@example.org")
user3 = User("carlos_b", "Carlos", "Barbosa", "carlos.barbosa@gmail.com")
user4 = User("anasilva89", "Ana", "Silva", "ana.silva@yahoo.com")

# Chamando métodos para verificar os dados de cada usuário
print("=== User 1 ===")
user1.describe_user()
user1.greet_user()

print("\n=== User 2 ===")
user2.describe_user()
user2.greet_user()

print("\n=== User 3 ===")
user3.describe_user()
user3.greet_user()

print("\n=== User 4 ===")
user4.describe_user()
user4.greet_user()