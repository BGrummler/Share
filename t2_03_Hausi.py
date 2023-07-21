"""
1) Definiere eine Funktion, welche zählt wie oft bestimmte Zeichen in
   einem string vorkommen. Dabei sollen die Zeichen, die gezählt werden
   beim Funktionsaufruf angegeben werden (=flexibel sein).
   
   z.B. f("Python", "y") -> {"y": 1}
        f("Banane", "a", "n", "e") -> {"a": 2, "n": 2, "e": 1}
        f("Tisch", "x", "y") -> {"x": 0, y: 0}
"""

def get_chars(word: str, *chars: str) -> dict:
    '''
    count occurences of chars in a word    

    Arguments:
        word: string to be searched
        *args: letters to be searching for   

    Returns: 
        dictionary with letters as keys and integers as amount value    
    '''
    dict_result = {}
    for letter in set(chars):
        dict_result[letter] = 0
    for elem in word:
        if elem in dict_result: dict_result[elem] += 1
    return dict_result

print(get_chars("Python", "y")) #-> {"y": 1}
print(get_chars("Banane", "a", "n", "e")) #-> {"a": 2, "n": 2, "e": 1}
print(get_chars("Tisch", "x", "y")) #-> {"x": 0, y: 0}
print(get_chars("Tisch",))
"""
2) Dokumentiere die Funktionen mit einem Docstring.

def new_range(*args):
    if len(args) == 1:    
        i = 0
        while i < args[0]:
            i += 1
            yield i 
    elif len(args) == 2:
        i = args[0]
        while i < args[1]:
            i += 1
            yield i
    elif len(args) == 3:
        i = args[0]
        while i < args[1]:
            i += args[2]
            yield i
    else: raise Exception ("to many args")

[print(chr(elem)) for elem in new_range(8)]
[print(chr(elem)) for elem in new_range(3,8)]
[print(elem) for elem in new_range(3,8,0.5)]
"""