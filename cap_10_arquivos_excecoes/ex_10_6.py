print("This app sums two numbers.")

first_number = input("Type first number: ")
second_number = input("Type second number: ")

try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print("You entered strings instead of numbers.")
else:
    result = first_number + second_number
    print("The sum is:", result)