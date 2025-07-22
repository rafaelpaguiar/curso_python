active = True
survey = {}

while active:
    name = input('What\'s your name? : ')
    place = input('Where do you dream to travel: : ')
    survey[name] = place
    
    continue_survey = input('Do you want to keep taking this survey? : ').lower()
    if continue_survey == 'no': 
        active = False
        print()

print("-------------------")
for name, place in survey.items():
    print(f"{name.title()} dreams to travel to {place}")

