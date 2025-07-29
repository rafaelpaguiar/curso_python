from pathlib import Path

print("Enter your guest list, type any time 'q' to quit.")

guest = ''
guest_list = ''

while guest != 'q':
    guest = input("Enter guest: ")
    if guest != 'q':
        guest_list += guest + "\n"

path = Path('guest_book.txt')
path.write_text(guest_list)
    