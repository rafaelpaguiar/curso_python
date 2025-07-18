glossary = {
    'for': 'how to repeat a block of code N times',
    'if': 'how to check a condition and execute a block of code based '
    'in the conditon result',
    'variable': 'how to keep a value for multiple uses in code',
    'set': 'a list of unordered unique itens ',
    'dictionary': 'a collection of key, value pairs',
    }

for key, value in glossary.items():
    print(f"{key.title()} : {value.title()}\n" )
