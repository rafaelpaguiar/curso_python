from pathlib import Path
import json


path = Path('favorite_number.json')

if path.exists():
    path = Path('favorite_number.json')
    content = json.loads(path.read_text())
    print(f"Your favorite number is {content}")
else:
    favorite_number = input("Whats your favorite number?: ")
    favorite_number = json.dumps(favorite_number)

    path.write_text(favorite_number)
    print("Number saved.")



