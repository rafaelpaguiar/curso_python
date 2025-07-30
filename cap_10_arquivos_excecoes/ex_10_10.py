from pathlib import Path

def count_ocurrences(path, word):

    result = 0

    try:
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} doesn't exist.")
    else:
        lines = content.splitlines()
        for line in lines:
            line = line.lower()
            count = line.count(word)
            result += count
        print(f"The word {word} occurs {result} in {path}")

files = ['gulliver.txt', 'frankstein.txt', 'moby_dick.txt']

for file in files:
    file_path = Path(file)
    count_ocurrences(file_path, 'whale')



    