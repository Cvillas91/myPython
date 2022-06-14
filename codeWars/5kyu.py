''' 
Moving Zeros To The End
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

Example: move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''
def move_zeros(arr):
    new = []
    zeros = []
    for el in arr:
        if el != 0:
            new.append(el)
        else:
            zeros.append(el)
    return new + zeros


''' 
ROT13
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Example: rot13("Test") # returns "Grfg"
'''

def rot13(message):
    dict = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z',
            'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
            'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z',
            'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M',}
    final = []
    for el in message:
        try:
            final.append(dict[el])
        except:
            final.append(el)
    return "".join(final)

''' 
Pete, the baker
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. 
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns 
the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts 
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.

Examples:
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''

def cakes(recipe, available):
    new = []
    for el in recipe:
        if el not in available:
            return 0
        else:
            new.append(available[el]//recipe[el])
    return min(new)


''' 
String incrementer
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Attention: If the number has leading zeros the amount of digits should be considered.

Examples:
    foo -> foo1
    foobar23 -> foobar24
    foo0042 -> foo0043
    foo9 -> foo10
    foo099 -> foo100
'''
def increment_string(strng):
    if strng == '': return '1'
    
    bln = True
    i = 1
    while bln and i <= len(strng):
        if strng[-i] in '1234567890':
            i += 1
        else:
            bln = False

    goodsubst = strng[len(strng)-i + 1:]
    new = []
    for el in goodsubst:
        if el in '1234567890': new.append(el)

    if len(new) == 0: new.append('0')
    return strng.replace("".join(new), '') + '0' * (len("".join(new)) - len(str(int("".join(new)) + 1))) + str(int("".join(new)) + 1)

''' 
Simple Pig Latin
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples:
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
'''
def pig_it(text):
    arr_inv = []
    arr = text.split(" ")
    for el in arr:
        if el[-1] not in '!.?#$%^&*':
            arr_inv.append(el[1:] + el[0] + 'ay')
        else:
            arr_inv.append(el[1:] + el[0])
    final = " ".join(arr_inv)
    return final

''' 
Valid Parentheses
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.

Examples
    "()"              =>  true
    ")(()))"          =>  false
    "("               =>  false
    "(())((()())())"  =>  true
'''
def valid_parentheses(string):
    txt = ''
    flag = True
    for el in string:
        if el == '(' or el == ')':
            txt += el
    if txt == '': return True
    while flag:
        if txt.find('()') == -1:
            return False
        else:
            txt = txt.replace('()','')
            if txt == '': return True
                
''' 
The Hashtag Generator
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''
def generate_hashtag(s):
    list = s.split()
    final = '#'
    for el in list:
        final += el.capitalize()
    if final == '#':
        return False
    elif len(final) > 140:
        return False
    else:
        return final
    
''' 
First non-repeating character
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that 
is not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character, 
but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("") or None
'''
def first_non_repeating_letter(string):
    string2 = string.lower()
    i = 0
    for char in string2:
        if string2.count(char) == 1:
            return string[i]
        else:
            i += 1
    return ''
''' 
Human Readable Time
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
'''
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds - (hours * 3600)) // 60
    sec = seconds - (hours * 3600) - (minutes * 60)
    fin = ''
    if len(str(hours)) == 2:
        fin += str(hours)
    else:
        fin += '0' + str(hours)
    if len(str(minutes)) == 2:
        fin += ':' + str(minutes)
    else:
        fin += ':0' + str(minutes)
    if len(str(sec)) == 2:
        fin += ':' + str(sec)
    else:
        fin += ':0' + str(sec)
    
    return fin

''' 
ROT13
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? 
According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.
Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.

Test examples:
"EBG13 rknzcyr." --> "ROT13 example."
"This is my first ROT13 excercise!" --> "Guvf vf zl svefg EBG13 rkprepvfr!"
'''
def rot13(message):
    normal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    rotten = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    rotmessage = ''
    for el in message:
        try:
            rotmessage += rotten[normal.index(el)]
        except:
            rotmessage += el
        
    return rotmessage
