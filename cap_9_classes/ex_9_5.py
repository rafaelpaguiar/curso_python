class User:
    def __init__(self,user_name,first_name,last_name,email):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User name : {self.user_name}")
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"E-mail : {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("jdoe123", "John", "Doe", "jdoe@example.com")


user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
print("\nReseting login attempts.\n")
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")
