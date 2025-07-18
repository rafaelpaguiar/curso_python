favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

participants = ['rafael', 'jen', 'edward', 'rachel']

for participant in participants:
    if participant in favorite_languages.keys():
        print("Thank you for your response.")
    else:
        print("Please take a few minutes to take our survey.")