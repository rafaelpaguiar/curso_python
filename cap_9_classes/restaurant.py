class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open now.")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type,flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("\nFlavors:\n--------------")
        for flavor in self.flavors:
            print(flavor.title())





