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

class Admin(User):

    def __init__(self,user_name,first_name,last_name,email,privileges):
        super().__init__(user_name,first_name,last_name,email)
        self.privileges = privileges
    
    def show_privileges(self):
        print("\nPrivileges\n----------")
        for privilege in self.privileges:
            print(privilege)


user1 = Admin("jdoe123", "John", "Doe", "jdoe@example.com", ["can add post","can update post", "can delete post"])

print("=== User 1 ===")
user1.describe_user()
user1.greet_user()
user1.show_privileges()
