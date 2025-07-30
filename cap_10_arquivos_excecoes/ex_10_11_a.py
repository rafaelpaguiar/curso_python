from pathlib import Path
import json

favorite_number = input("Whats your favorite number?: ")
favorite_number = json.dumps(favorite_number)
path = Path('favorite_number.json')
path.write_text(favorite_number)
print("Number saved.")
