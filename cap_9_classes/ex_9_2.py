class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a(n) {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open now.")


restaurant_01 = Restaurant('Isakaiada', 'Japanese')
restaurant_01.describe_restaurant()

restaurant_02 = Restaurant('Mamamia', 'Italian')
restaurant_02.describe_restaurant()

restaurant_03 = Restaurant('Maktub', 'Arab')
restaurant_03.describe_restaurant()
