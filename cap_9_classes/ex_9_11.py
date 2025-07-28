from users import Admin

user1 = Admin("jdoe123", "John", "Doe", "jdoe@example.com", ["can add post","can update post", "can delete post"])

print("=== User 1 ===")
user1.describe_user()
user1.greet_user()
user1.privileges.show_privileges()
