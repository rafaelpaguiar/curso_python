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

class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges\n----------")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):

    def __init__(self,user_name,first_name,last_name,email,privileges):
        super().__init__(user_name,first_name,last_name,email)
        self.privileges = Privileges(privileges)   
