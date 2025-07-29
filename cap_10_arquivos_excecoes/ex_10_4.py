from pathlib import Path

guest = input("Hi, what's your name?: ")

path = Path('guests.txt')
path.write_text(guest)