class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open now.")


restaurant = Restaurant('Isakaiada', 'Japanese')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
