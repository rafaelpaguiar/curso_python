def make_sandwich(name, *fillings):
    print(f"\n Making a {name.title()} with the following fillings:")
    for filling in fillings:
        print(f"- {filling}")

make_sandwich("Classic Ham and Cheese Sandwich",
              "sliced ham",
              "prato cheese",
              "lettuce",
              "tomato slices",
              "mayonnaise")

make_sandwich("Natural Chicken Sandwich",
              "shredded chicken",
              "grated carrot",
              "mayonnaise",
              "sweet corn",
              "iceberg lettuce",
              "whole wheat bread")

make_sandwich("Caprese Sandwich",
              "fresh mozzarella",
              "tomato slices",
              "fresh basil leaves",
              "olive oil",
              "ciabatta bread")