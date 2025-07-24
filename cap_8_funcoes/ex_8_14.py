def register_car(manufactor, model, **car):
        car['manufactor'] = manufactor
        car['model'] = model
        return car

car1 = register_car("Toyota", "Corolla")
print(car1)

car2 = register_car("Ford", "Focus", color="blue", year=2022)
print(car2)

car3 = register_car("Tesla", "Model 3", electric=True, autopilot=True, range_km=500)
print(car3)

