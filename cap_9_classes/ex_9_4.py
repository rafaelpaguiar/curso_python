class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open now.")

    def show_served(self):
        print(f"It served {self.number_served} client(s).")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,increment):
        self.number_served += increment

restaurant = Restaurant('Isakaiada', 'Japanese')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.number_served)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.show_served()
print("Setting number_served to 15:")
restaurant.set_number_served(15)
restaurant.show_served()
print("Incrementing number_served by 7:")
restaurant.increment_number_served(7)
restaurant.show_served()