from pathlib import Path
import json


user = {"username": "rafael",
        "first_name": "Rafael", 
        "last_name": "Aguiar", 
        "email": "rafael@email.com", 
        "age": 40,
        }

user_json = json.dumps(user)

path = Path('users.json')

if path.exists():
    user_json = json.loads(path.read_text())
    print(user_json)
else:
    path.write_text(user_json)

