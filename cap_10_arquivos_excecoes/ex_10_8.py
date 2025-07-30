from pathlib import Path

try:
    cats = Path('cats.txt')
    dogs = Path('dogs.txt')
    bugs = Path('bugs.txt')
    cats_content = cats.read_text()
    dogs_content = dogs.read_text()
    #bugs_content = bugs.read_text()
except FileNotFoundError:
    print("One of the files was not found.")
else:
    print(cats_content,end='\n')
    print(dogs_content)