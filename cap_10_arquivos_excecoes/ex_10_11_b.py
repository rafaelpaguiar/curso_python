from pathlib import Path
import json

path = Path('favorite_number.json')
content = json.loads(path.read_text())

print(f"Your favorite number is {content}")
