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
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

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
'''
Scramblies
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be 
rearranged to match str2, otherwise returns false.

Notes:
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.

Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''
def scramble(s1, s2):
    s3 = 'abcdefghijklmnopqrstuvwxyz'
    for char in s3:
        if s1.count(char) < s2.count(char):
            return False
    return True

'''
Number of trailing zeros of N!
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
'''
def zeros(n, fact = 0):
    newN = n // (5)
    newN1 = n / (5)
    fact += newN
    if newN1 < 1:
        return fact
    else:
        return zeros(newN1, fact)
    
'''
Tic-Tac-Toe Checker
f we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? 
Our goal is to create a function that will check that for us!
Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", 
or 2 if it is an "O", like so:
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
 
We want our function to return:
-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
'''
def is_solved(board):
    if board[0][0] == board[0][1] == board[0][2] == 1: return 1
    if board[0][0] == board[0][1] == board[0][2] == 2: return 2
    if board[1][0] == board[1][1] == board[1][2] == 1: return 1
    if board[1][0] == board[1][1] == board[1][2] == 2: return 2
    if board[2][0] == board[2][1] == board[2][2] == 1: return 1
    if board[2][0] == board[2][1] == board[2][2] == 2: return 2
    
    if board[0][0] == board[1][0] == board[2][0] == 1: return 1
    if board[0][0] == board[1][0] == board[2][0] == 2: return 1
    if board[0][1] == board[1][1] == board[2][1] == 1: return 1
    if board[0][1] == board[1][1] == board[2][1] == 2: return 1
    if board[0][2] == board[1][2] == board[2][2] == 1: return 1
    if board[0][2] == board[1][2] == board[2][2] == 2: return 1

    if board[0][0] == board[1][1] == board[2][2] == 1: return 1
    if board[0][0] == board[1][1] == board[2][2] == 2: return 1

    zeros = board[0].count(0) + board[1].count(0) + board[2].count(0)
    if zeros > 0:
        return -1
    else:
        return 0

'''
Product of consecutive Fib numbers
The Fibonacci numbers are the numbers in the following integer sequence (Fn):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
F(n) * F(n+1) = prod.
Your function productFib takes an integer (prod) and returns an array:
[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prod 
you will return [F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod.

Example:

productFib(714) # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
'''
def Fibo(n):
    dict = {0:0, 1:1}
    i = 0
    while i <= n:
        if i not in dict:
            dict.update({i:dict[i-1] + dict[i-2]})
        i += 1
    return dict[n]
           
def productFib(prod, i = 0):
    n0 = Fibo(i)
    n1 = Fibo(i + 1)
    while n1 * n0 <= prod:
        if n1 * n0 == prod:
            return [n0, n1, True]
        else:
            i += 1
            n0 = Fibo(i)
            n1 = Fibo(i + 1)
    return [n0, n1, False]

'''
Pascal's Diagonals
Create a function that returns an array containing the first l numbers from the nth diagonal of Pascal's triangle.

n = 0 should generate the first diagonal of the triangle (the ones).
The first number in each diagonal should be 1.
If l = 0, return an empty array.
'''
def generate_diagonal(n, l):
    arr = []
    fin = []
    for i in range(1, l + n + 1):
        new = []
        C = 1
        for j in range(1, i + 1):
            new.append(C)
            C = C *(i-j) // j
        arr.append(new)
    
    j = 0
    for i in range(n, l + n):
            fin.append(arr[i][j])
            j += 1

    return fin

'''
Luck check
In some countries of former Soviet Union there was a belief about lucky tickets. 
A transport ticket of any sort was believed to posess luck if sum of digits on the left half of 
its number was equal to the sum of digits on the right half. Here are examples of such numbers:

003111    #             3 = 1 + 1 + 1
813372    #     8 + 1 + 3 = 3 + 7 + 2
17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6

Your task is to write a funtion luck_check(str), which returns true/True if argument is string 
decimal representation of a lucky ticket number, or false/False for all other numbers. 
It should throw errors for empty strings or strings which don't represent a decimal number.
'''
def luck_check(string):
    size = len(string) // 2
    sum1, sum2 = 0, 0
    for i in range(size):
        sum1 += int(string[i])
        sum2 += int(string[-i -1])
    return sum1 == sum2

'''
Find the Word Pair!
Given an array of words and a target compound word, your objective is to find the two words which combine into the target word, 
returning both words in the order they appear in the array, and their respective indices in the order they combine to form the 
target word. Words in the array you are given may repeat, but there will only be one unique pair that makes the target compound word. 
If there is no match found, return null/nil/None.
Note: Some arrays will be very long and may include duplicates, so keep an eye on efficiency.

Examples:
fn(['super','bow','bowl','tar','get','book','let'], "superbowl")      =>   ['super','bowl',   [0,2]]
fn(['bow','crystal','organic','ally','rain','line'], "crystalline")   =>   ['crystal','line', [1,5]]
fn(['bow','crystal','organic','ally','rain','line'], "rainbow")       =>   ['bow','rain',     [4,0]]
fn(['bow','crystal','organic','ally','rain','line'], "organically")   =>   ['organic','ally', [2,3]]
fn(['top','main','tree','ally','fin','line'], "mainline")             =>   ['main','line',    [1,5]]
fn(['top','main','tree','ally','fin','line'], "treetop")              =>   ['top','tree',     [2,0]]
'''
def compound_match(words, target):
    arr = []
    other = []
    for el in set(words):
        if el in target:
            for oel in set(words):
                if el + oel == target: 
                    arr.append(el)
                    arr.append(oel)
    try:
        other.append(words.index(arr[0]))
        other.append(words.index(arr[1]))
        return [words[min(other)], words[max(other)], other]
    except:
        return None

'''
Find the unique string
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. 
E.g. string that contains only spaces is like empty string.
'''
def find_uniq(arr):
    arr1 = "".join(arr)
    new = []
    min = 1000
    for el in set(arr1):
        if arr1.count(el) < min:
            min = arr1.count(el)
            aux = el
    for subel in arr:
        if aux in subel:
            return subel
        
'''
Maximum subarray sum
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. 
If the list is made up of only negative numbers, return 0 instead.
Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''
def max_sequence(arr):
    fin = []
    leng = len(arr)
    for i in range(0, leng + 1):
        for j in range(0, leng + 1):
            fin.append(sum(arr[i:j]))
    return max(fin)

'''
Scraping: Get the Year a CodeWarrior Joined
#Task: Write a function get_member_since which accepts a username from someone at Codewars and returns 
an string containing the month and year separated by a space that they joined CodeWars.

#Example:
>>> get_member_since('dpleshkov')
Jul 2016
>>> get_member_since('jhoffner')
Oct 2012
'''
from bs4 import BeautifulSoup
import urllib.request
def get_member_since(username):
    html_content = urllib.request.urlopen("https://www.codewars.com/users/" + username)
    soup = BeautifulSoup(html_content, "html.parser")
    stat = soup.find_all("div", class_="stat")
    for el in stat:
        if 'Member' in el.text: 
            stri = str(el.text)
    return stri.replace("Member Since:", "")

'''
Extract the domain name from a URL
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
'''
def domain_name(url):
    url = url.replace("https://", "").replace("http://", "").replace("www.", "")
    arr = url.split(".")
    return arr[0]

'''
Excel's COUNTIF, SUMIF and AVERAGEIF functions
##The Brief Microsoft Excel provides a number of useful functions for counting, summing, and averaging values if they meet a 
certain criteria. Your task is to write three functions that work similarly to Excel's COUNTIF, SUMIF and AVERAGEIF functions.

##Specifications Each function will take the same two arguments:
A list object containing values to be counted, summed, or averaged.
A criteria in either an integer, float, or string
Integer or float indicates equality
Strings can indicate >, >=, <, <= or <> (use the Excel-style "Not equal to" operator) to a number (ex. ">=3"). 
In the count_if function, a string without an operater indicates equality to this string.
The tests will all include properly formatted inputs. The test cases all avoid rounding issues associated with floats.

##Examples
count_if([1,3,5,7,9], 3) --> 1
count_if(["John","Steve","John"], "John") --> 2
sum_if([2,4,6,-1,3,1.5],">0") --> 16.5
average_if([99,95.5,0,83],"<>0") --> 92.5
'''
def count_if(values,criteria):
    sum = 0
    if '>=' in str(criteria):
        for value in values:
            if value >= float(criteria.replace('>=','')):
                sum += 1
    elif '<=' in str(criteria):
        for value in values:
            if value <= float(criteria.replace('<=','')):
                sum += 1
    elif '<>' in str(criteria):
        for value in values:
            if value != float(criteria.replace('<>','')):
                sum += 1            
    elif '>' in str(criteria):
        for value in values:
            if value > float(criteria.replace('>','')):
                sum += 1
    elif '<' in str(criteria):
        for value in values:
            if value < float(criteria.replace('<','')):
                sum += 1
    else:
        for value in values:
            if value == criteria:
                sum += 1
    return sum
    

def sum_if(values,criteria):
    sum = 0
    if '>=' in str(criteria):
        for value in values:
            if value >= float(criteria.replace('>=','')):
                sum += value
    elif '<=' in str(criteria):
        for value in values:
            if value <= float(criteria.replace('<=','')):
                sum += value
    elif '<>' in str(criteria):
        for value in values:
            if value != float(criteria.replace('<>','')):
                sum += value            
    elif '>' in str(criteria):
        for value in values:
            if value > float(criteria.replace('>','')):
                sum += value
    elif '<' in str(criteria):
        for value in values:
            if value < float(criteria.replace('<','')):
                sum += value
    else:
        for value in values:
            if value == criteria:
                sum += value
    return sum
    
def average_if(values,criteria):
    sum = 0
    count = 0
    if '>=' in str(criteria):
        for value in values:
            if value >= float(criteria.replace('>=','')):
                sum += value
                count += 1
    elif '<=' in str(criteria):
        for value in values:
            if value <= float(criteria.replace('<=','')):
                sum += value
                count += 1
    elif '<>' in str(criteria):
        for value in values:
            if value != float(criteria.replace('<>','')):
                sum += value    
                count += 1
    elif '>' in str(criteria):
        for value in values:
            if value > float(criteria.replace('>','')):
                sum += value
                count += 1
    elif '<' in str(criteria):
        for value in values:
            if value < float(criteria.replace('<','')):
                sum += value
                count += 1
    else:
        for value in values:
            if value == criteria:
                sum += value
                count += 1
    return sum/count

'''
okkOokOo
We've got a message from the Librarian. 
As usual there're many o and k in it and, as all codewarriors don't know "Ook" language we need that you translate this message.
tip : it seems traditional "Hello World!" would look like : 
Ok, Ook, Ooo?  Okk, Ook, Ok?  Okk, Okk, Oo?  Okk, Okk, Oo?  Okk, Okkkk?  Ok, Ooooo?  Ok, Ok, Okkk?  Okk, Okkkk?  Okkk, Ook, O?  
Okk, Okk, Oo?  Okk, Ook, Oo?  Ook, Ooook!

Your task is to implement a function okkOokOo(okkOookk), that would take the okkOookk message as input and return a decoded 
human-readable string.

eg:
okkOokOo('Ok, Ook, Ooo!')  # -> 'H'
okkOokOo('Ok, Ook, Ooo?  Okk, Ook, Ok?  Okk, Okk, Oo?  Okk, Okk, Oo?  Okk, Okkkk!')  # -> 'Hello'
okkOokOo('Ok, Ok, Okkk?  Okk, Okkkk?  Okkk, Ook, O?  Okk, Okk, Oo?  Okk, Ook, Oo?  Ook, Ooook!')  # -> 'World!'
'''
def okkOokOo(s):
    words = s.replace(" ", "").split("?")
    fin = ""
    for el in words:
        new_el = "0b" + el.lower().replace("o","0").replace("k","1").replace(",","").replace("!","")
        fin += (chr(eval(new_el)))
    return fin

'''
All that is open must be closed...
We all know about "balancing parentheses" (plus brackets, braces and chevrons) and even balancing characters that are identical.
Read that last sentence again, I balanced different characters and identical characters twice and you didn't even notice... :)
Kata
Your challenge in this kata is to write a piece of code to validate that a supplied string is balanced.
You must determine if all that is open is then closed, and nothing is closed which is not already open!
You will be given a string to validate, and a second string, where each pair of characters defines an opening and closing sequence 
that needs balancing.
You may assume that the second string always has an even number of characters.

Example
# In this case '(' opens a section, and ')' closes a section
is_balanced("(Sensei says yes!)", "()")       # => True
is_balanced("(Sensei says no!", "()")         # => False

# In this case '(' and '[' open a section, while ')' and ']' close a section
is_balanced("(Sensei [says] yes!)", "()[]")   # => True
is_balanced("(Sensei [says) no!]", "()[]")    # => False

# In this case a single quote (') both opens and closes a section
is_balanced("Sensei says 'yes'!", "''")       # => True
is_balanced("Sensei say's no!", "''")         # => False
'''
def is_balanced(source, caps):

    dict ={}
    j = 0
    for i in range(0, int(len(caps)/2)):
        dict[caps[j]] = caps[j + 1]
        j += 2

    only = ''

    for el in source:
        if el in caps:
            only += el
    if len(only) % 2 != 0:
        return False
    else:
        for h in range(len(dict)):
            only = only.replace(list(dict.keys())[h] + dict[list(dict.keys())[h]], '')
        if len(only) % 2 != 0:  return False
        mid_l = int(len(only)/2) - 1
        mid_r = int(len(only)/2)
        for i in range(0, mid_r):
            if dict[only[mid_l - i]] != only[mid_r + i]:
                return False
    
        return True
    
'''
Perimeter of squares in a rectangle
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum 
of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 
Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares 
disposed in the same manner as in the drawing:

alternative text
Hint:
See Fibonacci sequence

The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) 
and returns the total perimeter of all the squares.

perimeter(5)  should return 80
perimeter(7)  should return 216
'''
def perimeter(n):
    fin = [1]
    a, b = 1, 1
    for i in range(n):
        fin.append(b)
        a, b = b, a + b
    return sum(fin) * 4

'''
Bulk up!
Given an array of meals where each element is a string in the form '300g turkey, 300g potatoes, 100g cucumber' find out 
how many proteins and calories you consumed. You like to keep things simple so all values will be expressed in grams. 
In case you didn't know every gram of protein and carbohydrate has 4 calories, while 1 gram of fat provides 9 calories.
An object food (in Ruby $food ) is preloaded for you that contains the information about the given food per 100 grams:
food = { 
  "chicken": [20, 5, 10], # per 100g chicken has 20g of protein, 5 grams of carbohydrates and 10 grams of fat.
  "eggs": [10, 5, 15],    # protein:10g , carbs:5g , fats: 15g
  "salmon": [27, 0, 10], 
  "beans": [8, 25, 0], 
  "bananas": [1, 23, 0], 
  ... 
  ... }
Round your results to 2 decimal places and return a string in the form "Total proteins: n grams, Total calories: n".
Delete all trailing zeros on every float and remove trailing point if the result is an integer. Note: No invalid input testing.
'''
def bulk(arr):
    print(arr)
    prot, cal = 0, 0
    if arr == []: 
        return 'Total proteins: 0 grams, Total calories: 0'
    else:
        new = ",".join(arr).replace(", ",",")
        s = new.split(",")
        for el in s:
            aux = el.split(" ")
            grams = int(aux[0].replace("g",""))
            prot += food[aux[1]][0] * grams / 100
            cal += food[aux[1]][0] * grams / 100 * 4
            cal += food[aux[1]][1] * grams / 100 * 4
            cal += food[aux[1]][2] * grams / 100 * 9    
        prot = f'{str(prot).rstrip("0").rstrip(".") if "." in str(prot) else prot}'
        cal = f'{str(cal).rstrip("0").rstrip(".") if "." in str(cal) else cal}'
        return f"Total proteins: {prot} grams, Total calories: {cal}"

'''
Value of x
Jack's teacher gave him a ton of equations for homework. The thing is they are all kind of same so they are boring.
So help him by making a equation solving function that will return the value of x.

Test Cases will be like this:
# INPUT            # RETURN
'x + 1 = 9 - 2'    # 6
'- 10 = x'         # -10
'x - 2 + 3 = 2'    # 1
'- x = - 1'        # 1
All test cases are valid.
Every +, - and numbers will be separated by space.
There will be only one x either on the left or right.
x can have a - mark before it.
returned object will be a integer.
'''
def solve(eq: str):
    flag = False
    if "- x" in eq: 
        print('h')
        flag = True
        eq = eq.replace("- x", "x")
        
    eq = eq.replace("- ", "-").replace("+ ","")
        
    ind = eq.index("=")
    le, ri = [], []
    le, ri = eq[:ind], eq[ind + 1:]
    aLe = le.split(" ")
    aRi = ri.split(" ")

    if 'x' in aLe:
        sum1 = sum([int(x) for x in aRi if x != ''])
        aLe.pop(aLe.index('x'))
        sum2 = sum([int(x) for x in aLe if x != ''])
    else:
        sum1 = sum([int(x) for x in aLe if x != ''])
        aRi.pop(aRi.index('x'))
        sum2 = sum([int(x) for x in aRi if x != ''])
    
    if flag == True:
        return (sum1 - sum2) * - 1
    else:
        return sum1 - sum2

'''
80's Kids #6: Rock 'Em, Sock 'Em Robots
You and your friends have been battling it out with your Rock 'Em, Sock 'Em robots, 
but things have gotten a little boring. You've each decided to add some amazing new features to your robot and automate them
to battle to the death.
Each robot will be represented by an object. 
You will be given two robot objects, and an object of battle tactics and how much damage they produce. 
Each robot will have a name, hit points, speed, and then a list of battle tacitcs they are to perform in order.
Whichever robot has the best speed, will attack first with one battle tactic.

Your job is to decide who wins.
Example:

 robot_1 = {
  "name": "Rocky",
  "health": 100,
  "speed": 20,
  "tactics": ["punch", "punch", "laser", "missile"]
 }
 robot_2 = {
   "name": "Missile Bob",
   "health": 100,
   "speed": 21,
   "tactics": ["missile", "missile", "missile", "missile"]
 }
 tactics = {
   "punch": 20,
   "laser": 30,
   "missile": 35
 }
 
fight(robot_1, robot_2, tactics) -> "Missile Bob has won the fight."
robot2 uses the first tactic, "missile" because he has the most speed. This reduces robot1's health by 35. 
Now robot1 uses a punch, and so on.

Rules
A robot with the most speed attacks first. If they are tied, the first robot passed in attacks first.
Robots alternate turns attacking. Tactics are used in order.
A fight is over when a robot has 0 or less health or both robots have run out of tactics.
A robot who has no tactics left does no more damage, but the other robot may use the rest of his tactics.
If both robots run out of tactics, whoever has the most health wins. Return the message "{Name} has won the fight."
If both robots run out of tactics and are tied for health, the fight is a draw. Return "The fight was a draw."
'''
def fight(r1, r2, t):
    mxTacR1 = len(r1['tactics'])
    mxTacR2 = len(r2['tactics'])
    round = 1
    while True:
        if round > mxTacR1 or round > mxTacR2:
            if r1['health'] == r2['health']: 
                if mxTacR2 > mxTacR1:
                    return f"{r2['name']} has won the fight."
                else:
                    return "The fight was a draw."
            if r1['health'] > r2['health']: 
                return f"{r1['name']} has won the fight."
            else:
                return f"{r2['name']} has won the fight."
        if r1['speed'] >= r2['speed']:
            r2['health'] -= t[r1['tactics'][round - 1]]
            if r2['health'] <= 0:
                return f"{r1['name']} has won the fight."
            else:
                r1['health'] -= t[r2['tactics'][round - 1]]
                if r1['health'] <= 0:
                    return f"{r2['name']} has won the fight."
                round += 1
        else:
            r1['health'] -= t[r2['tactics'][round - 1]]
            if r1['health'] <= 0:
                return f"{r2['name']} has won the fight."
            else:
                r2['health'] -= t[r1['tactics'][round - 1]]
                if r2['health'] <= 0:
                    return f"{r1['name']} has won the fight."
                round += 1
       
