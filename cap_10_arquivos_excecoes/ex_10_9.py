from pathlib import Path

try:
    cats = Path('cats.txt')
    cats_content = cats.read_text()
except FileNotFoundError:
    pass
else:
    print(cats_content,end='\n')

try:
    dogs = Path('dogs.txt')
    dogs_content = dogs.read_text()
except FileNotFoundError:
    pass
else:
    print(dogs_content,end='\n')

try:
    bugs = Path('bugs.txt')
    bugs_content = bugs.read_text()
except FileNotFoundError:
    pass
else:
    print(bugs_content,end='\n')