from users import User

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
