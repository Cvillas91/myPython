'''
Sum of Digits / Digital Root
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.

Examples:
16  -->  1 + 6 = 7
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
'''
def digital_root(n):
    strD = str(n)
    sum = 0
    print(len(strD))
    if len(strD) >= 2:
        for el in strD:
            sum += int(el)
        return digital_root(int(sum))
    else:
        return n
    
'''
Counting Duplicates
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits 
that occur more than once in the input string. The input string can be assumed to contain only alphabets 
(both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''
def duplicate_count(text):
    sum = 0
    new = [1]
    counted = []
    setU = ''.join(set(text))
    setU = setU.lower()
    for char in setU:
        if char not in counted:
            counted.append(char)
            new.append(text.lower().count(char))
    for el in new:
        if el > 1: sum +=1
    return sum

'''
Find The Parity Outlier
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''
def find_outlier(int):
    new =  [0 if x == 0 or x % 2 == 0 else 1 for x in int]
    if new.count(1) == 1:
        return int[new.index(1)]
    else:
        return int[new.index(0)]
    
'''
Duplicate Encoder
The goal of this exercise is to convert a string to a new string where each character in the new 
string is "(" if that character appears only once in the original string, or ")" if that character appears 
more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
    "din"      =>  "((("
    "recede"   =>  "()()()"
    "Success"  =>  ")())())"
    "(( @"     =>  "))((" 
'''
def duplicate_encode(word):
    word = word.lower()
    final = ''
    for el in word:
        if word.count(el) > 1:
            final += ')'
        else:
            final += '('
    return final

'''
Tribonacci Sequence
As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the
sequence to generate the next
So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31, ...]

But what if we started with [0, 0, 1] as a signature? 
As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, 
you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a 
signature array/list, returns the first n elements - signature included of the so seeded sequence.
'''
def tribonacci(s, n):
    nterms = n
    n1, n2, n3 = s[0], s[1], s[2] 
    count = 0

    if nterms <= 0:
        return []
    elif nterms == 1:
        return [n1]
    elif nterms == 2:
        return [n1, n2]
    elif nterms == 3:
        return [n1, n2, n3]
    else:
        arr = []
        while count < nterms:
            arr.append(n1)
            nth = n1 + n2 + n3
            # update values
            n1 = n2
            n2 = n3
            n3 = nth
            count += 1
    return arr

'''
Your order, please
Your task is to sort a given string. Each word in the string will contain a single number. 
This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''
def order(sentence):
    s = sentence.split(" ")
    fin = []
    for i in range(1, len(s) + 1):
        for el in s:
            if str(i) in el:
                fin.append(el)
    return " ".join(fin)

'''
Your order, please
You are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
'''
def alphabet_position(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    new = []
    for char in text.lower():
        try:
            new.append(str(letters.index(char) + 1))
        except: 
            pass
    
    return " ".join(new)

'''
Unique In Order
Implement the function unique_in_order which takes as argument a sequence and returns a list of 
items without any elements with the same value next to each other and preserving the original order of elements.

For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
'''
def unique_in_order(iterable):
    if iterable == '': return []
    new = [iterable[0]]
    for el in iterable:
        if new[-1] != el:
            new.append(el)
    return new

'''
Persistent Bugger
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
''' 
def persistence(n, per = 0):
    if len(str(n)) == 1:
        return per
    else:
        newN = 1
        for char in str(n):
            newN *= int(char)
        return persistence(newN, per + 1)
    
'''
+1 Array
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
The array can't be empty
Only non-negative, single digit integers are allowed
Return nil (or your language's equivalent) for invalid inputs.

Examples
For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
[4, 3, 2, 5] would return [4, 3, 2, 6]
''' 
def up_array(arr):
    if arr == []: return None
    try:
        new = ''
        final = []
        for el in arr:
            if el >= 10: return None
            new += str(el)
        new = str(int(new) + 1)
        for el in new:
            final.append(int(el))
        return final
    except:
        return None
    
'''
Line Up
There are several units in a line, out of your sight. You will be given a list of hints (a list or array of strings) that 
indicates who is next to who in the queue, and you have to rebuild the queue of people, in appropriate order.
Example
With these hints,

["white has black on his left",
 "red has green on his right",
  "black has green on his left"]
you should reduce that the queue is the following:

["red", "green", "black", "white"]
Notes:
It is always possible to reduce the complete order in the queue.
The hints can be of two different forms, such as "white has black on his left", or "black has white on his right".
Each queue has at least two units.
''' 
def line_up(hints):
    final = []
    forHints = []
    dict = {}
    for hint in hints:
        forHints.append(hint.split(" "))
        
    for i in range(len(forHints)):
        if forHints[i][5] == 'right':
            if forHints[i][0] not in dict.keys():
                dict[forHints[i][0]] = forHints[i][2]
        elif forHints[i][5] == 'left':
            if forHints[i][2] not in dict.keys():
                dict[forHints[i][2]]= forHints[i][0]
                
    for i in range(len(forHints)):
        if forHints[i][0] not in dict.values():
            seed = forHints[i][0]
        if forHints[i][2] not in dict.values():
            seed = forHints[i][2]
    
    final.append(seed)
    for i in range(len(dict)):
        final.append(dict[final[i]])
    
    return final

'''
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
You will always get an valid array. And it will be always exactly one letter be missing. 
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Examples:
['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
''' 
def find_missing_letter(chars):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    seed = chars[0].lower()
    start = abc.index(seed)
    for i in range(len(chars)):
        if chars[i].lower() == abc[start + i]:
            pass
        else:
            return abc[start + i].upper() if chars[0].isupper() else abc[start + i]
        
'''
Highest Scoring Word
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
'''         
def high(x):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    arr = x.split(' ')
    dict = {}
    max = 0 
    equ = ''
    for el in arr:
        sum = 0
        for i in range(len(el)):
            sum += alphabet.index(el[i]) + 1
        dict[el] = sum
    for key in dict:
        if dict[key] > max:
            max = dict[key]
            equ = key
    return equ

'''
Reverse or rotate?
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) 
of size sz (ignore the last chunk if its size is less than sz).
If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, 
reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return 
the result as a string.

If
    sz is <= 0 or if str is empty return ""
    sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
Examples:
    revrot("123456987654", 6) --> "234561876549"
    revrot("123456987653", 6) --> "234561356789"
    revrot("66443875", 4) --> "44668753"
    revrot("66443875", 8) --> "64438756"
    revrot("664438769", 8) --> "67834466"
    revrot("123456779", 8) --> "23456771"
    revrot("", 8) --> ""
    revrot("123456779", 0) --> "" 
    revrot("563000655734469485", 4) --> "0365065073456944"
'''  
def rev_rot(strng, sz):
    if sz <= 0 or strng == '' or sz > len(strng): return ''
    chunks = len(strng) // sz
    arr = []
    j = 0
    
    for i in range(chunks):
        arr.append(strng[i + j:sz + i + j])
        j += sz - 1
    
    arr2 = []
    for el in arr:
        sum = 0
        for i in range(len(el)):
            sum += int(el[i]) ** 3
        if sum % 2 == 0:
            arr2.append(el[::-1])
        else:
            arr2.append(el[1:] + el[0])
    return "".join(arr2)

'''
Split Strings
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second 
character of the final pair with an underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
'''
def solution(s):
    arr = []
    j = 0
    for i in range(0, len(s) // 2 ):
        arr.append(s[j:j + 2])
        j += 2
            
    if len(s) / 2 - len(s) // 2 != 0:
        arr.append(s[-1] + "_")
    
    return arr

'''
Sort the odd
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the 
even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
'''
def sort_array(arr):
    aux = []
    fin = []
    for el in arr:
        if el % 2 != 0:
            aux.append(el)
    aux.sort()
    
    i = 0
    for el in arr:
        if el % 2 == 0:
            fin.append(el)
        else:
            fin.append(aux[i])
            i += 1
    return fin

'''
Valid Braces
Write a function that takes a string of braces, and determines if the order of the braces is valid. 
It should return true if the string is valid, and false if it's invalid.
All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''
def valid_braces(string):
    dict = {'(' : ')', '{' : '}', '[' : ']', ')' : '1', '}' : '1', ']' : '1'}
    if string == '': return True
    print(string, string[-2])
    try:
        if dict[string[0]] == string[1]:
            string = string[2:]
            return valid_braces(string)
        elif dict[string[-2]] == string[-1]:
            string = string[:-2]
            return valid_braces(string)
        elif dict[string[0]] == string[-1]:
            string = string[1:-1]
            return valid_braces(string)
        else:
            return False
    except:
        return False

'''
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form.
For example:
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
'''
def expanded_form(num):
    strNum = str(num)
    fin = ''
    for i in range(len(strNum)):
        if strNum[i] != '0':
            fin += strNum[i] + '0' * (len(strNum) - i - 1) + ' + '
    return fin[:-3]

'''
Write Number in Expanded Form - Part 2
You will be given a number and you will need to return it as a string in expanded form.
For example:

expanded_from(807.304); // Should return "800 + 7 + 3/10 + 4/1000"
expanded_from(1.24); // should return "1 + 2/10 + 4/100"
expanded_from(7.304); // should return "7 + 3/10 + 4/1000"
expanded_from(0.04); // should return "4/100"
'''
def expanded_form(num):
    strNum = str(num).split('.')
    fin = ''
    for i in range(len(strNum[0])):
        if strNum[0][i] != '0':
            fin += strNum[0][i] + '0' * (len(strNum[0]) - i - 1) + ' + '
    for i in range(len(strNum[1])):
        if strNum[1][i] != '0':
            fin += strNum[1][i] + '/1' + '0' * (i + 1) + ' + '
    return fin[:-3]

'''
Mexican Wave
In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 
 1.  The input string will always be lower case but maybe empty.
 2.  If the character in the string is whitespace then pass over it as if it was an empty seat
Example: wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
'''
def wave(people):
    new = []
    l = len(people)
    for i in range(0, l):
        aux = ''
        for j in range(0, len(people)):
            if i == j:
                aux += people[j].upper()
            else:
                aux += people[j]
        new.append(aux)
    fin = []
    for el in new:
        if el != people:
            fin.append(el)
    return fin
            
'''
Difference of 2
The objective is to return all pairs of integers from a given array of integers that have a difference of 2.
The result array should be sorted in ascending order of values.
Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.

Examples
[1, 2, 3, 4]  should return [(1, 3), (2, 4)]
[4, 1, 2, 3]  should also return [(1, 3), (2, 4)]
[1, 23, 3, 4, 7] should return [(1, 3)]
[4, 3, 1, 5, 6] should return [(1, 3), (3, 5), (4, 6)]
'''
def twos_difference(lst): 
    lst = sorted(lst)
    arr = []
    for el in lst:
        if el + 2 in lst:
            if (el, el + 2) not in arr and (el + 2, el) not in arr:
                li = (el, el + 2)
                arr.append(li)

    return arr

'''
Count letters in string
You've to count lowercase letters in a given string and return the letter count in a hash with 'letter' as key and count 
as 'value'.

Example:
letter_count('arithmetics') #=> {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}
'''
def letter_count(s):
    hash = {}
    for el in list(set(sorted(s))):
        hash[el] = s.count(el)
    return hash

'''
Count characters in your string
The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''
def count(string):
    dict = {}
    s = set(string)
    for el in s:
        dict[el] = string.count(el)
    return dict

'''
Playing with digits
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive 
integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
In other words:
Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
If it is the case we will return k, if not return -1.
Note: n and p will always be given as strictly positive integers.
dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
'''
def dig_pow(n, p):
    sum = 0
    for el in str(n):
        sum += int(el) ** p
        p += 1
    return sum/n if sum/n - sum//n == 0 else -1

'''
Build Tower
Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
'''
def tower_builder(n):
    lng = (n * 2) - 1
    fin = []
    for i in range(0 , n):
        sp = (lng // 2) - i
        star = (lng // 2) - sp
        str = sp * ' ' + star * '*' + '*' + star * '*' + sp * ' '
        fin.append(str)
    return fin

'''
Triple trouble
Write a function triple_double(num1, num2) which takes numbers num1 and num2 and returns 1 if there is a straight 
triple of a number at any place in num1 and also a straight double of the same number in num2.

If this isn't the case, return 0
Examples
triple_double(451999277, 41177722899) == 1
# num1 has straight triple 999s and num2 has straight double 99s
triple_double(1222345, 12345) == 0
# num1 has straight triple 2s but num2 has only a single 2
'''

def triple_double(num1, num2):
    num1, num2 = str(num1), str(num2)
    for i in range(0, 10):
        if str(i) * 3 in num1 and str(i) * 2 in num2:
            return 1
    return 0

'''
Twisted Sum
Find the sum of the digits of all the numbers from 1 to N (both ends included).

Examples
# N = 4
1 + 2 + 3 + 4 = 10
# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46
# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
'''
def compute_sum(n):
    sum = 0
    for i in range(0, n + 1):
        num = str(i)
        for el in num:
            sum += int(el)
    return sum

'''
Srot the inner ctonnet in dsnnieedcg oredr
You have to sort the inner content of every word of a string in descending order.
The inner content is the content of a word without first and the last char.
Some examples:

"sort the inner content in descending order"  -->  "srot the inner ctonnet in dsnnieedcg oredr"
"wait for me"        -->  "wiat for me"
"this kata is easy"  -->  "tihs ktaa is esay"
Words are made up of lowercase letters.
'''
def sort_the_inner_content(words):
    fin = []
    arr = words.split(" ")
    for el in arr:
        if len(el) > 1:
            m = "".join(sorted(el[1:-1], reverse = True))
            fin.append(el[0] + m + el[-1])
        else:
            fin.append(el)
    return " ".join(fin)

'''
Alphabetized
Re-order the characters of a string, so that they are concatenated into a new string in 
"case-insensitively-alphabetical-order-of-appearance" order. 
Whitespace and punctuation shall simply be removed!
The input is restricted to contain no numerals and only words containing the english alphabet letters.

Example:
alphabetized("The Holy Bible") # "BbeehHilloTy"
'''
def alphabetized(s):
    f= 'z'
    for char in s:
        if char.isalpha():
            for i in range(len(f)):
                if char.lower() < f[i]:
                    f = char + f
                    quit()
    return f[:-1]
                    
'''
Where is my parent!?(cry)
Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. 
All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. 
But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.

Legend:
-Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
-Function input: String contains only letters, uppercase letters are unique.
Task:
Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".
'''
def find_children(d):
    fin = ''
    for el in sorted(set((d.upper()))):
        fin += el + d.count(el.lower()) * el.lower()
    return fin
    
'''
Dashatize it
Given a variable n,
If n is an integer, Return a string with dash'-'marks before and after each odd integer, 
but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.
If n is not an integer, return the string "None".

Ex:
dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
'''
def dashatize(n):
    if n == 0: return '0'
    fin = ''
    if type(n) == int:
        for char in str(abs(n)):
            if int(char) % 2 == 1:
                fin += '-' + char + '-'
            else:
                fin += char

        fin = fin.replace('--','-')

        if fin[0] == '-':
            fin = fin[1:]
        if fin[-1] == '-':
            fin = fin[:-1]
        return fin
                
    else:
        return 'None'

'''
Lottery Ticket
Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the jackpot.

Example ticket:
[ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
To do this, you must first count the 'mini-wins' on your ticket. 
Each subarray has both a string and a number within it. 
If the character code of any of the characters in the string matches the number, you get a mini win. 
Note you can only have one mini win per sub array.

Once you have counted all of your mini wins, compare that number to the other input provided (win). 
If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

All inputs will be in the correct format. Strings on tickets are not always the same length.
'''
def bingo(ticket,win):
    miniw = 0
    for el in ticket:
        if chr(el[1]) in el[0]:
            miniw += 1
    return 'Winner!' if miniw >= win else 'Loser!'
            
'''
String Breakers
I will give you an integer (N) and a string. 
Break the string up into as many substrings of N as you can without spaces. 
If there are leftover characters, include those as well.

Example: 

n = 5;

st = "This is an example string";

Return value:
Thisi
sanex
ample
strin
g

Return value as a string: 'Thisi'+'\n'+'sanex'+'\n'+'ample'+'\n'+'strin'+'\n'+'g'
'''
def string_breakers(n, st): 
    st = st.replace(" ", "")
    new = ''
    
    for i in range(1, len(st) + 1):
        if i % n == 0:
            new += st[i - 1] + '\n'
        else:
            new += st[i - 1]
    
    if new[-1:] == '\n': new = new[:-1] 
    
    return  new
            
'''
Consonant value
Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. 
Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"
-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. The highest is 26.
solve("zodiacs") = 26
For the word "strength", solve("strength") = 57
-- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. 
The highest is 57.
'''
def solve(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s = s.replace('a',' ').replace('e',' ').replace('i',' ').replace('o',' ').replace('u',' ')
    fin = s.split(" ")
    rrr = []
    for el in fin:
        sum = 0
        for subel in el:
            sum += alpha.index(subel) + 1
        rrr.append(sum)
        
    return max(rrr)

'''
Reverse every other word in the string
Reverse every other word in a given string, then return the string. 
Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. 
Punctuation marks should be treated as if they are a part of the word in this kata.
'''
def reverse_alternate(string):
    new = string.split(" ")
    fin = []
    i = 1
    for el in new:
        if el != '':
            if i % 2 != 0:
                fin.append(el)
            else:
                fin.append(el[::-1])
            i += 1
    return " ".join(fin)

'''
Anagram difference
Given two words, how many letters do you have to remove from them to make them anagrams?
Example
First word : c od e w ar s (4 letters removed)
Second word : ha c k er r a nk (6 letters removed)
Result : 10
'''
def anagram_difference(w1, w2):
    w1 = list(w1)
    w2 = list(w2)
    sum = 0
    for el in w1:
        if el in w2:
            w2.pop(w2.index(el))
            sum += 1
    return len(w2) + len(w1) - sum

'''
Dead Ants
An orderly trail of ants is marching across the park picnic area.
It looks something like this:
..ant..ant.ant...ant.ant..ant.ant....ant..ant.ant.ant...ant..
But suddenly there is a rumour that a dropped chicken sandwich has been spotted on the ground ahead. 
The ants surge forward! Oh No, it's an ant stampede!!
Some of the slower ants are trampled, and their poor little ant bodies are broken up into scattered bits.
The resulting carnage looks like this:
...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t
Can you find how many ants have died?
'''
def dead_ant_count (ants):
    maxx = max(ants.count('a') ,ants.count('n'),ants.count('t'))
    return maxx - ants.count('ant') 

'''
Find the Mine!
You've just discovered a square (NxN) field and you notice a warning sign. 
The sign states that there's a single bomb in the 2D grid-like field in front of you.
Write a function mineLocation/MineLocation that accepts a 2D array, and returns the location of the mine. 
The mine is represented as the integer 1 in the 2D array. Areas in the 2D array that are not the mine will be represented as 0s.
The location returned should be an array (Tuple<int, int> in C#) where the first element is the row index, 
and the second element is the column index of the bomb location (both should be 0 based). All 2D arrays passed into your 
function will be square (NxN), and there will only be one mine in the array.

Examples:
mineLocation( [ [1, 0, 0], [0, 0, 0], [0, 0, 0] ] ) => returns [0, 0]
mineLocation( [ [0, 0, 0], [0, 1, 0], [0, 0, 0] ] ) => returns [1, 1]
mineLocation( [ [0, 0, 0], [0, 0, 0], [0, 1, 0] ] ) => returns [2, 1]
'''
def mineLocation(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                return [i, j]

'''
Permute a Palindrome
Write a function that will check whether ANY permutation of the characters of the input string is a palindrome. 
Bonus points for a solution that is efficient and/or that uses only built-in language functions. 
Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.

Examples
madam -> True
adamm -> True
junk -> False
'''
def permute_a_palindrome (input): 
    map = set(input)
    flag = 0
    for el in map:
        if input.count(el) % 2 != 0:
            flag += 1
        if flag > 1: return False
    return True

'''
Duplicate Arguments
Complete the solution so that it returns true if it contains any duplicate argument values. 
Any number of arguments may be passed into the function.
The array values passed in will only be strings or numbers. 
The only valid return values are true and false.

Examples:
solution(1, 2, 3)             -->  false
solution(1, 2, 3, 2)          -->  true
solution('1', '2', '3', '2')  -->  true
'''
def solution(*args):
    for el in args:
        if args.count(el) > 1:
            return True
    return False

'''
Don't Drink the Water

Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear in the 
glass based on their density. (Lower density floats to the top) The width of the glass will not change from top to bottom.

======================
|   Density Chart    |
======================
| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |
----------------------

[                            [
 ['H', 'H', 'W', 'O'],        ['O','O','O','O']
 ['W', 'W', 'O', 'W'],  =>    ['W','W','W','W']
 ['H', 'H', 'O', 'O']         ['H','H','H','H']
 ]                           ]
 
The glass representation may be larger or smaller. If a liquid doesn't fill a row, it floats to the top and to the left.
'''
def separate_liquids(glass):
    if glass == []: return []
    hs, os, als, ws = 0, 0, 0, 0
    st = ''
    new = []
    size = len(glass[0])
    for level in glass:
        for el in level:
            if el == "H":
                hs += 1
            elif el == "W":
                ws += 1
            elif el == "A":
                als += 1
            else:
                os += 1
    st = os * 'O' + als * 'A' + ws * 'W' + hs * 'H'
    
    for i in range(len(glass)):
        aux = []
        for j in range(size):
            aux.append(st[0])
            st = st[1:]
        new.append(aux)
        
    return new
                
'''
Custom FizzBuzz Array

Write a function that returns a (custom) FizzBuzz sequence of the numbers 1 to 100.

The function should be able to take up to 4 arguments:

The 1st and 2nd arguments are strings, "Fizz" and "Buzz" by default;
The 3rd and 4th arguments are integers, 3 and 5 by default.
Thus, when the function is called without arguments, it will return the classic FizzBuzz sequence up to 100:

[ 1, 2, "Fizz", 4, "Buzz", "Fizz", 7, ... 14, "FizzBuzz", 16, 17, ... 98, "Fizz", "Buzz" ]
When the function is called with (up to 4) arguments, it should return a custom FizzBuzz sequence, for example:

('Hey', 'There')      -->  [ 1, 2, "Hey", 4, "There", "Hey", ... ]
('Foo', 'Bar', 2, 3)  -->  [ 1, "Foo", "Bar", "Foo", 5, "FooBar", 7, ... ]
Examples
fizz_buzz_custom()[15]                         # returns 16
fizz_buzz_custom()[44]                         # returns "FizzBuzz" (45 is divisible by 3 and 5)
fizz_buzz_custom('Hey', 'There')[25]         # returns 26
fizz_buzz_custom('Hey', 'There')[11]         # returns "Hey" (12 is divisible by 3)
fizz_buzz_custom("What's ", "up?", 3, 7)[80] # returns "What's " (81 is divisible by 3)
The function must return the sequence as a list.
'''
def fizz_buzz_custom(string_one = 'Fizz', string_two = 'Buzz', num_one = 3, num_two = 5): 
    fin = []
    for i in range(1, 101):
        if i % num_one == 0:
            if i % num_two == 0:
                fin.append(string_one + string_two)
            else:
                fin.append(string_one)
        elif i % num_two == 0:
            fin.append(string_two)
        else:
            fin.append(i)
    return fin

'''
Christmas tree
Create a function that returns a christmas tree of the correct height.
For example: height = 5 should return:

    *    
   ***   
  *****  
 ******* 
*********

Height passed is always an integer between 0 and 100.

Use \n for newlines between each line.
Pad with spaces so each line is the same length. The last line having only stars, no spaces.
'''
def christmas_tree(height):
    tree = ''
    if height == 0: tree = ''
    for i in range(1, height + 1):
        tree += ' ' * (height - i) +  (i - 1) * '*' + '*' + (i - 1) * '*' + ' ' * (height - i) + '\n'
    return tree[:-1]

'''
Complete Fibonacci Series
The function 'fibonacci' should return an array of fibonacci numbers. 
The function takes a number as an argument to decide how many no. of elements to produce. 
If the argument is less than or equal to 0 then return empty array

Example:
fibonacci(4) # should return  [0,1,1,2]
fibonacci(-1) # should return []
'''
def fibonacci(n):
    dict = {0:0, 1:1}
    fin = []
    if n <= 0: return fin
    for i in range(0, n):
        if i not in dict.keys():
            dict[i] = dict[i-1] + dict[i-2]
            fin.append(dict[i])
        else:
            fin.append(dict[i])
    return fin

'''
N-th Fibonacci
I love Fibonacci numbers in general, but I must admit I love some more than others.
I would like for you to write me a function that when given a number (n) returns the n-th number in the Fibonacci Sequence.

For example:
   nth_fib(4) == 2
'''
def nth_fib(n):
    a, b = 0, 1
    if n == 1: return a
    for i in range(1, n - 1):
        a, b = b, a + b
    return b

'''
Which are in?
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are 
substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
returns []
'''
def in_array(array1, array2):
    new, fin = [], []
    for el in array1:
        for el2 in array2:
            if el in el2:
                new.append(el)
    for el in set(new):
        fin.append(el)
    return sorted(fin)

'''
Two Sum
Write a function that takes an array of numbers (integers for the tests) and a target number. 
It should find two different items in the array that, when added together, give the target value. 
The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; 
target will always be the sum of two different items from that array).

two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]
'''
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                if target - numbers[i] == numbers[j]:
                    return (j, i)

'''
WeIrD StRiNg CaSe
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all 
even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. 
The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper 
cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). 
Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
'''
def to_weird_case(words):
    new = words.split(" ")
    out = []
    for el in new:
        out.append(twc(el))
    return " ".join(out)

def twc(word):
    fin = ''
    for i in range(0, len(word)):
        if i % 2 == 0:
            fin += word[i].upper()
        else:
            fin += word[i].lower()
    return fin

'''
first character that repeats
Find the first character that repeats in a String and return that character.

first_dup('tweet') => 't'
first_dup('like') => None
This is not the same as finding the character that repeats first. In that case, an input of 'tweet' would yield 'e'.

Another example:
In 'translator' you should return 't', not 'a'.
v      v  
translator
  ^   ^
While second 'a' appears before second 't', the first 't' is before the first 'a'.
'''
def first_dup(s):
    fin = []
    for el in s:
        if s.count(el) > 1:
            fin.append(el)
    try:
        return fin[0]
    except:
        return None
    
'''
Integer depth
The depth of an integer n is defined to be how many multiples of n it is necessary to compute before all 10 digits have appeared at least once in some multiple.

example:

let see n=42
Multiple         value         digits     comment
42*1              42            2,4 
42*2              84             8         4 existed
42*3              126           1,6        2 existed
42*4              168            -         all existed
42*5              210            0         2,1 existed
42*6              252            5         2 existed
42*7              294            9         2,4 existed
42*8              336            3         6 existed 
42*9              378            7         3,8 existed
Looking at the above table under digits column you can find all the digits from 0 to 9, 
Hence it required 9 multiples of 42 to get all the digits. So the depth of 42 is 9. 
Write a function named computeDepth which computes the depth of its integer argument.Only positive numbers greater than zero will be passed as an input.
'''
def compute_depth(n):
    cre = ''
    depth = 0
    while True:
        depth += 1
        sg = str(n * depth)
        for el in sg:
            if el not in cre:
                cre += el
        if len(cre) == 10: return depth

'''
Compare Versions
Karan's company makes software that provides different features based on the version of operating system of the user.
For finding which version is more recent, Karan uses the following method:
While this function worked for OS versions 10.6, 10.7, 10.8 and 10.9, the Operating system company just released OS version 10.10.
Karan's function fails for the new version:
compare_versions ("10.9", "10.10");       # returns True, while it should return False
Karan now wants to spend some time to write a more robust version comparison function that works for any future version/sub-version updates.

Help Karan write this function. Here are a few sample cases:
compare_versions("11", "10");                    # returns True
compare_versions("11", "11");                    # returns True
compare_versions("10.4.6", "10.4");              # returns True
compare_versions("10.4", "11");                  # returns False
compare_versions("10.4", "10.10");               # returns False
compare_versions("10.4.9", "10.5");              # returns False
It can be assumed that version strings are non empty and only contain numeric literals and the character '.'.
'''
def compare_versions(v1, v2):
    v1 = list(v1.split("."))
    v2 = list(v2.split("."))
    for i in range(0, max(len(v1), len(v2))):
        try: 
            c1 = int(v1[i])
        except:
            c1 = 0
        try: 
            c2 = int(v2[i])
        except:
            c2 = 0
        if c1 < c2:
            return False
    return True

'''
Check if two words are isomorphic to each other
Two strings a and b are called isomorphic if there is a one to one mapping possible for every character of a to every character of b. 
And all occurrences of every character in a map to same character in b.
Task
In this kata you will create a function that return True if two given strings are isomorphic to each other, and False otherwise. 
Remember that order is important.
Your solution must be able to handle words with more than 10 characters.

Example
True:
CBAABC DEFFED
XXX YYY
RAMBUNCTIOUSLY THERMODYNAMICS

False:
AB CC
XXY XYY
ABAB CD
'''
def isomorph(a, b):
    if len(a) != len(b):
        return False
    dict = {}
    for i in range(0, len(a)):
        if a[i] not in dict.keys():
            dict[a[i]] = b[i]
    word = ''
    
    d_swap = {v: k for k, v in dict.items()}
    

    for i in range(0, len(b)):
        try:
            word += d_swap[b[i]]
        except:
            return False
    
    return word == a
        
'''
Highest Rank Number in an Array
Complete the method which returns the number which is most frequent in the given input array. 
If there is a tie for most frequent number, return the largest number among them.
Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
'''
def highest_rank(arr):
    dict = {}
    for el in set(arr):
        dict[el] = arr.count(el)
    high = 0
    num = 0
    for el in sorted(set(arr)):
        if dict[el] >= high:
            if el > num:
                high = dict[el]
                num = el
    return num

'''
Numericals of a String
You are given an input string.
For each symbol in the string if it's the first character occurrence, replace it with a '1', else replace it with the amount of times you've already seen it.

Examples:
input   =  "Hello, World!"
result  =  "1112111121311"
input   =  "aaaaaaaaaaaa"
result  =  "123456789101112"
There might be some non-ascii characters in the string.
'''
def numericals(s):
    dict = {}
    fin = ''
    for el in s:
        if el not in dict.keys():
            fin += '1'
            dict[el] = 1
        else:
            dict[el] = dict[el] + 1
            fin += str(dict[el])
    return fin

'''
A disguised sequence (I)
Given u0 = 1, u1 = 2 and the relation 6unun+1-5unun+2+un+1un+2 = 0 calculate un for any integer n >= 0.

Examples:
Call fcn the function such as fcn(n) = un.
fcn(17) -> 131072; fcn(21) -> 2097152

Remark:
You can take two points of view to do this kata:
the first one purely algorithmic from the definition of un
the second one - not at all mandatory, but as a complement - is to get a bit your head around and find which sequence is hidden behind un.
'''
def fcn (n):
    print(n)
    dict = {0: 1, 1: 2}
    for i in range(n + 1):
        if i not in dict.keys():
            dict[i] = -6 * dict[i-2] * dict[i-1]//(-5 * dict[i-2] + dict[i-1])
    return dict[n]

'''
Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.
As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.
If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
'''
def longest_palindrome (s):
    large, count = 0, 0
    for i in range(0, len(s)+1):
        for j in range(i, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                count = max(count, len(s[i:j]))
    return count

'''
Who won the election?
In democracy we have a lot of elections. For example, we have to vote for a class representative in school, 
for a new parliament or a new government.
Usually, we vote for a candidate, i.e. a set of eligible candidates is given. 
This is done by casting a ballot into a ballot-box. 
After that, it must be counted how many ballots (= votes) a candidate got.
A candidate will win this election if he has the absolute majority.

Your Task
Return the name of the winner. If there is no winner, return null / nil / None depending on the language.
Task Description
There are no given candidates. An elector can vote for anyone. Each ballot contains only one name and represents one vote for this name. 
A name is an arbitrary string, e.g. "A", "B", or "XJDHD". There are no spoiled ballots.
The ballot-box is represented by an unsorted list of names. Each entry in the list corresponds to one vote for this name. 
You do not know the names in advance (because there are no candidates).
A name wins the election if it gets more than n / 2 votes (n = number of all votes, i.e. the size of the given list).

Examples
# 3 votes for "A", 2 votes for "B"  -->  "A" wins the election
["A", "A", "A", "B", "B"]  -->  "A"

# 2 votes for "A", 2 votes for "B"  -->  no winner
["A", "A", "B", "B"]  -->  None / nil / null

# 1 vote for each name --> no winner
["A", "B", "C", "D"]  -->  None / nil / null

# 3 votes for "A", 2 votes for "B", 1 vote for "C"  -->  no winner, as "A" does not have more than n / 2 = 3 votes
["A", "A", "A", "B", "B", "C"] -->  None / nil / null
'''
def get_winner(ballots):
    winners = []
    maj = len(ballots) / 2
    for el in set(ballots):
        if ballots.count(el) > maj:
            winners.append(el)
    if len(winners) != 1:
        return None
    else:
        return winners[0]

'''
Simple Sentences
Implement a function, so it will produce a sentence out of the given parts.

Array of parts could contain:

words;
commas in the middle;
multiple periods at the end.
Sentence making rules:

there must always be a space between words;
there must not be a space between a comma and word on the left;
there must always be one and only one period at the end of a sentence.

Example:
makeSentence(['hello', ',', 'my', 'dear']) // returns 'hello, my dear.'
'''
def make_sentences(parts):
    fin = ''
    for el in parts:
        if el == ',':
            fin += el
        elif el == '.':
            pass
        else:
            fin += ' ' + el
    return fin[1:] + '.'

'''
N smallest elements in original order
Your task is to write a function that does just what the title suggests 
(so, fair warning, be aware that you are not getting out of it just throwing a lame bas sorting method there) 
with an array/list/vector of integers and the expected number n of smallest elements to return.

Also:
the number of elements to be returned cannot be higher than the array/list/vector length;
elements can be duplicated;
in case of duplicates, just return them according to the original order (see third example for more clarity).
Same examples and more in the test cases:

first_n_smallest([1,2,3,4,5],3) == [1,2,3]
first_n_smallest([5,4,3,2,1],3) == [3,2,1]
first_n_smallest([1,2,3,4,1],3) == [1,2,1]
first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
first_n_smallest([1,2,3,4,5],0) == []
'''
def first_n_smallest(arr, n):
    x = sorted(arr)[0:n]
    y = []
    for el in x:
        y.append(arr.index(el))
        arr[arr.index(el)] = 'x'
    return [i for _, i in sorted(zip(y, x))]

'''
Numerical Palindrome #2
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. 
Examples of numerical palindromes are:

2332
110011
54322345

For this kata, single digit numbers will not be considered numerical palindromes.
For a given number num, write a function to test if the number contains a numerical palindrome 
or not and return a boolean (true if it does and false if does not). Return "Not valid" if the input is not an integer 
or is less than 0.

Note: Palindromes should be found without permutating num.

palindrome(5) => false
palindrome(1221) => true
palindrome(141221001) => true
palindrome(1215) => true 
palindrome(1294) => false 
palindrome("109982") => "Not valid"
'''
def palindrome(num):
    if type(num) == int and num > 0:
        for i in range(0, len(str(num))):
            for j in range(i + 1, len(str(num))):
                if str(num)[i:j + 1] == str(num)[i:j + 1][::-1]:
                    return True
        return False
    return 'Not valid'

'''
String average
You are given a string of numbers between 0-9. 
Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. 
Eg: "zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"
'''
def average_string(s):
    dict = {"one": 1, 1: "one", "two": 2, 2: "two", "three": 3, 3: "three", \
           "four": 4, 4: "four", "five": 5, 5: "five", "six": 6, 6: "six", \
           "seven":7, 7: "seven", "eight": 8, 8: "eight", "nine": 9, 9: "nine", \
           "zero": 0, 0: "zero"}
    new = s.split(" ")
    av = 0
    for el in new:
        try:
            av += dict[el]
        except:
            return "n/a"
    return dict[av // len(new)]

'''
Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
The number 898989 is the first integer with more than one digit that fulfills the property partially 
introduced in the title of this kata. What's the use of saying "Eureka"? 

Examples
1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range [a,b][a, b][a,b] the function should output an empty list.
90, 100 --> []
'''
def sum_dig_pow(a, b):
    fin = []
    for i in range(a, b + 1):
        if check(i):
            fin.append(i)
    return fin
        
        
def check(n):
    sum = 0
    s = str(n)
    i = 1
    for el in s:
        sum += int(el) ** i
        i += 1
    if sum == n:
        return True
    else:
        return False

'''
Frog jumping
You have an array of integers and have a frog at the first position
[Frog, int, int, int, ..., int]

The integer itself may tell you the length and the direction of the jump
For instance:
 2 = jump two indices to the right
-3 = jump three indices to the left
 0 = stay at the same position
Your objective is to find how many jumps are needed to jump out of the array.

Return -1 if Frog can't jump out of the array

Example:
array = [1, 2, 1, 5]; 
jumps = 3  (1 -> 2 -> 5 -> <jump out>)
'''
def solution(a):
    count = 0
    pos = 0
    
    while True:
        if pos < len(a) and pos >= 0 and count <= len(a):
            pos += a[pos]
            count += 1
        else:
            break
    return count if count <= len(a) else -1

'''
Inside Out Strings
You are given a string of words (x), for each word within the string you need to turn the word 'inside out'. 
By this I mean the internal letters will move out, and the external letters move toward the centre.

If the word is even length, all letters will move. 
If the length is odd, you are expected to leave the 'middle' letter of the word where it is.

An example should clarify:
'taxi' would become 'atix' 'taxis' would become 'atxsi'
'''
def inside_out(st):
    words = st.split(" ")
    fin = []
    for el in words:
        fin.append(wch(el))
    return " ".join(fin)
    
def wch(st):
    l = len(st) // 2
    if len(st) % 2 == 0:
        return st[:l][::-1] + st[l:][::-1]
    elif len(st) == 1:
        return st
    else:
        return st[:l][::-1] + st[l] + st[l + 1:][::-1]

'''
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!

You have to write a method, that return the length of the missing array.
Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3
If the array of arrays is null/nil or empty, the method should return 0.
When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays.
Have fun coding it and please don't forget to vote and rank this kata! :-)
I have created other katas. Have a look if you like coding and challenges.
'''
def get_length_of_missing_array(a):
    if a == [] or None in a: return 0
    fin = []
    for el in a:
        if el == []: return 0
        fin.append(len(el))
    for i in range(min(fin), max(fin) + 1):
        if i not in fin:
            return i
        
'''
Autocomplete! Yay!
The autocomplete function will take in an input string and a dictionary array and return the values 
from the dictionary that start with the input string. If there are more than 5 matches, restrict your output 
to the first 5 results. If there are no matches, return an empty array.

Example:
autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
'''
def autocomplete(inp, dict):
    new = ''
    for el in inp:
        if el.isalpha(): new += el
        
    lg = len(new)
    fin = []
    for el in dict:
        if el.lower()[:lg] == new.lower():
            fin.append(el)
    return fin[:5]

'''
Kebabize
Modify the kebabize function so that it converts a camel case string into a kebab case.
kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:
the returned string should only contain lowercase letters
'''
def kebabize(s):
    fin = []
    word = ''
    for el in s:
        if el.isalpha():
            if el.islower():
                word += el
            else:
                fin.append(word) if word != '' else False
                word = el.lower()
    fin.append(word)
    return "-".join(fin)

'''
Equal Sides Of An Array
You are going to be given an array of integers. Your job is to take that array and find an index N 
where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. 
If there is no index that would make this happen, return -1.

For example:
Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left 
side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left side 
of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Last one:
You are given the array {20,10,-80,10,10,15,35}
At index 0 the left side is {}
The right side is {10,-80,10,10,15,35}
They both are equal to 0 when added. (Empty arrays are equal to 0 in this problem)
Index 0 is the place where the left side and right side are equal.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

Input:
An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output:
The lowest index N where the side to the left of N is equal to the side to the right of N. 
If you do not find an index that fits these rules, then you will return -1.

Note:
If you are given an array with multiple answers, return the lowest correct index.
'''
def find_even_index(arr):
    l = len(arr)
    if sum(arr[1:]) == 0: return 0
    for i in range(1, l):
        if sum(arr[0 : i]) == sum(arr[i + 1:]):
            return i
    return -1

'''
Pascal's Triangle
In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula

Task
Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional list/array.

Example:
n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]
'''
import math
def pascals_triangle(n):
    fin = []
    for j in range(0, n):
        for i in range(0, j + 1):
            fin.append(fun(j,i))
            
    return fin

def fun(n, k):
    res1 = math.factorial(n)
    res2 = math.factorial(k)
    res3 = math.factorial(n-k)
    return res1//(res2 * res3)

'''
Simple Fun #79: Delete a Digit
Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example
For n = 152, the output should be 52;
For n = 1001, the output should be 101.

Input/Output
[input] integer n
Constraints: 10 ≤ n ≤ 1000000.
[output] an integer
'''
def delete_digit(n):
    s = list(str(n))
    max = 0
    for i in range(len(s)):
        it = s[i]
        s.pop(i)
        h = int("".join(s))
        print(h)
        if h > max: max = h
        s.insert(i, it)
    return max

'''
Shortest steps to a number
Given a number, num, return the shortest amount of steps it would take from 1, to land exactly on that number.

Description:
A step is defined as either:
Adding 1 to the number: num += 1
Doubling the number: num *= 2

You will always start from the number 1 and you will have to return the shortest count of steps it would 
take to land exactly on that number.

1 <= num <= 10000
Examples:
num == 3 would return 2 steps:

1 -- +1 --> 2:        1 step
2 -- +1 --> 3:        2 steps

num == 12 would return 4 steps:

1 -- +1 --> 2:        1 step
2 -- +1 --> 3:        2 steps
3 -- x2 --> 6:        3 steps
6 -- x2 --> 12:       4 steps
'''
def shortest_steps_to_num(num):
    step = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        step += 1
    return step

'''
Sum consecutives
You are given a list/array which contains only integers (positive and negative). 
Your job is to sum only the numbers that are the same and consecutive. 
The result should be one list.

#Examples:
[1,4,4,4,0,4,3,3,1] # should return [1,12,0,4,6,1]
[1,1,7,7,3] # should return [2,14,3]
[-5,-5,7,7,12,0] # should return [-10,14,12,0]
'''
def sum_consecutives(s):
    fin = []
    fact = 1
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            fact += 1
        else:
            fin.append(s[i] * fact)
            fact = 1
    fin.append(s[-1] * fact)
    return fin

'''
Consecutive strings
You are given an array(list) strarr of strings and an integer k. 
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:
treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".
'''
def longest_consec(s, k):
    l = len(s)
    mx = ''
    if k > l or k <= 0: 
        return ''
    elif k == 1:
        return max(s, key=len)
    else:
        for i in range(0, l - k + 1):
            word = ''
            for j in range(0, k):
                word += s[i + j]
            if len(word) > len(mx):
                mx = word
        return mx
    
'''
Build a pile of Cubes
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of 
If such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1
'''
def find_nb(m):
    sum = 0
    i = 1
    while True:
        if sum > m: 
            return -1
        else:
            sum += i ** 3
            if sum == m: return i
            i += 1
            
'''
Bouncing Balls
A child is playing with a ball on the nth floor of a tall building. The height of this floor above ground level, h, is known.
He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

Examples:
- h = 3, bounce = 0.66, window = 1.5, result is 3
- h = 3, bounce = 1, window = 1.5, result is -1 
(Condition 2) not fulfilled).
'''
def bouncing_ball(h, b, w):
    if b >= 1 or w >= h: return -1
    bt = h * b
    if bt < w: 
        return -1
    else:
        i = 1
        while bt > w:
            bt *= b
            i += 2
    return i

'''
Character with longest consecutive repetition
For a given string s find the character c (or C) with longest consecutive repetition and return: (c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.
For empty string return: ('', 0)
'''
from itertools import groupby

def longest_repetition(s):
    max, ss = 0, ''
    groups = groupby(s)
    result = [[label, sum(1 for _ in group)] for label, group in groups]
    for el in result:
        if el[1] > max:
            max = el[1]
            ss = el[0]
            
    return (ss, max)

'''
Make the Deadfish Swim
Write a simple parser that will parse and run Deadfish.
Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
'''
def parse(data):
    fin = []
    tot = 0
    for el in data:
        if el == 'i':
            tot += 1
        elif el == 'd':
            tot -= 1
        elif el == 's':
            tot = tot ** 2
        elif el == 'o':
            fin.append(tot)
        else:
            pass
    return fin
        
'''
Data Reverse
A stream of data is received and needs to be reversed.
Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
should become:
10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.

The data is given in an array as such:
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
'''
def data_reverse(data):
    nb = len(data) // 8
    fin = []
    for i in range(0, nb):
        byt = ''
        for j in range(0, 8):
            print(j +(8*i))
            byt += str(data[j + (8 * i)])
        fin.append(byt)
    s = "".join(fin[::-1])
    return [int(x) for x in s]

'''
Row of the odd triangle
Given a triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
find the triangle's row knowing its index (the rows are 1-indexed), e.g.:

odd_row(1)  ==  [1]
odd_row(2)  ==  [3, 5]
odd_row(3)  ==  [7, 9, 11]
Note: your code should be optimized to handle big inputs.
'''
def odd_row(n):
    fin = []
    ant = (n - 1) * n / 2
    fo =  ant * 2 + 1
    for i in range (0, n):
        fin.append(fo + (2 * i))
    return fin


'''
The Deaf Rats of Hamelin
How many deaf rats are there?
Legend
P = The Pied Piper
O~ = Rat going left
~O = Rat going right

Example
ex1 ~O~O~O~O P has 0 deaf rats
ex2 P O~ O~ ~O O~ has 1 deaf rat
ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats
'''
def count_deaf_rats(town):
    sum = 0
    town = town.replace(" ","")
    le, ri = [], []
    ind = town.index('P')
    le, ri = town[0:ind], town[ind + 1:len(town) + 1]
    
    for i in range(0, len(le), 2):
        if le[i] != '~':
            sum += 1
            
    for i in range(0, len(ri), 2):
        if ri[i] != 'O':
            sum += 1
            
    return sum

'''
More Zeros than Ones
Create a moreZeros function which will receive a string for input, and return an array (or null terminated string in C)
containing only the characters from that string whose binary representation of its ASCII value consists of more zeros than ones.
You should remove any duplicate characters, keeping the first occurrence of any such duplicates, so they are in the 
same order in the final array as they first appeared in the input string.

Examples

'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
               True       True       False      True       False
        --> ['a','b','d']
    
'DIGEST'--> ['D','I','E','T']
All input will be valid strings of length > 0. Leading zeros in binary should not be counted.
''' 
def more_zeros(s):
    fin = []
    for el in s:
        b = bin(ord(el))[2:]
        if b.count('0') > b.count('1'):
            c = chr(int('0b' + b, 2))
            if c not in fin:
                fin.append(c)
    return fin

'''
Evil Autocorrect Prank
Write a function called autocorrect that takes a string and replaces all instances of "you" or "u" 
(not case sensitive) with "your sister" (always lower case).

Return the resulting string.
Here's the slightly tricky part: These are text messages, so there are different forms of "you" and "u".
For the purposes of this kata, here's what you need to support:
"youuuuu" with any number of u characters tacked onto the end
"u" at the beginning, middle, or end of a string, but NOT part of a word
"you" but NOT as part of another word like youtube or bayou
''' 
def autocorrect(input):
    fin = []
    while True:
        if 'youu' in input or 'Youu' in input:
            input = input.replace('youu','you').replace('Youu', 'you')
        else:
            break
            
    s = input.split(" ")
    for el in s:
        if el.lower() in ('u', 'you'):
            fin.append('your sister')
        elif el.lower() == 'you!':
            fin.append('your sister!')
        else:
            fin.append(el)
    return " ".join(fin)

'''
Rectangle into Squares
The drawing below gives an idea of how to cut a given "true" rectangle into squares 
("true" rectangle meaning that the two dimensions are different).

You will be given two dimensions
a positive integer length
a positive integer width

sqInRect(5, 3) should return [3, 2, 1, 1]
sqInRect(3, 5) should return [3, 2, 1, 1]
''' 
def sq_in_rect(lng, wdth):
    arr = []
    if lng == wdth: return None
    while lng > 0 and wdth > 0:
        arr.append(wdth if lng > wdth else lng)
        if lng > wdth:
            lng -= wdth
        else:
            wdth -= lng
    return arr

'''
String array duplicates
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:
dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].
dup(["kelless","keenness"]) = ["keles","kenes"].
Strings will be lowercase only, no spaces. See test cases for more examples.
''' 
def dup(arry):
    fin = []
    dup = ' '
    for word in arry:
        for char in word:
            if dup[-1] != char:
                dup += char
        fin.append(dup[1:])
        dup = ' '
    return fin

'''
Basic Encryption
The most basic encryption method is to map a char to another char by a certain math rule. 
Because every char has an ASCII value, we can manipulate this value with a simple math expression. For example 'a' + 1 would give us 'b', 
because 'a' value is 97 and 'b' value is 98.

You will need to write a method which does exactly that -
get a string as text and an int as the rule of manipulation, and should return encrypted text. for example:

encrypt("a",1) = "b"
Full ascii table is used on our question (256 chars) - so 0-255 are the valid values.
If the value exceeds 255, it should 'wrap'. ie. if the value is 345 it should wrap to 89.
''' 
def encrypt(text, rule):
    new = ''
    if text == "": return ""
    for el in text:
        numb = (ord(el) + rule) 
        while numb > 255:
            numb -= 256
        new += chr(numb)
    
    return new
'''
Fold an array
In this kata you have to write a method that folds a given array of integers by the middle x-times.

An example says more than thousand words:
Fold 1-times:
[1,2,3,4,5] -> [6,6,3]
A little visualization (NOT for the algorithm but for the idea of folding):
 Step 1         Step 2        Step 3       Step 4       Step5
                     5/           5|         5\          
                    4/            4|          4\      
1 2 3 4 5      1 2 3/         1 2 3|       1 2 3\       6 6 3
----*----      ----*          ----*        ----*        ----*
Fold 2-times:
[1,2,3,4,5] -> [9,6]
As you see, if the count of numbers is odd, the middle number will stay. 
Otherwise the fold-point is between the middle-numbers, so all numbers would be added in a way.

The array will always contain numbers and will never be null. The parameter runs will always be a positive 
integer greater than 0 and says how many runs of folding your method has to do.
If an array with one element is folded, it stays as the same array.
''' 
def fold_array(a, runs):
    for i in range(runs):
        l = len(a)//2
        aux = []
        for j in range(l):
            aux.append(a[j] + a[-j-1]) 
        if len(a) % 2 != 0: aux.append(a[l])
        a = aux
    return a

'''
Encrypt this!
You want to create secret messages which can be deciphered by the Decipher this! kata. 
Here are the conditions:
Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.

Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
''' 
def encrypt_this(t):
    if t == "": return ""
    a = t.split(" ")
    fin = []
    for el in a:
        if len(el) == 1:
            fin.append(str(ord(el)))
        elif len(el) == 2:
            fin.append(str(ord(el[0])) + el[1])
        else:
            word = str(ord(el[0])) + el[-1] + el[2:-1] + el[1]
            fin.append(word)
    return " ".join(fin)

'''
English beggars
Born a misinterpretation of this kata, your task here is pretty simple: given an array of values and an amount of beggars, 
you are supposed to return an array with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.

For example: [1,2,3,4,5] for 2 beggars will return a result of [9,6], as the first one takes [1,3,5], the second collects [2,4].
The same array with 3 beggars would have in turn have produced a better out come for the second beggar: [5,7,3], as they will 
respectively take [1,4], [2,5] and [3].

Also note that not all beggars have to take the same amount of "offers",
meaning that the length of the array is not necessarily a multiple of n; length can be even shorter,
in which case the last beggars will of course take nothing (0).
''' 
def beggars(values, n):
    fin = []
    for i in range(n):
        sum = 0
        for j in range(i, len(values), n):
            sum += values[j]
        fin.append(sum)
    return fin

'''
Find the missing term in an Arithmetic Progression
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. 
You are provided with consecutive elements of an Arithmetic Progression.
There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you.
The rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers. 
The missing term will never be the first or last one.

Example
find_missing([1, 3, 5, 9, 11]) == 7
''' 
def find_missing(s):
    s = sorted(s)
    d = min(abs(s[0] - s[1]), abs(s[-1] - s[-2]))
    n = len(s) + 1
    ss = (n/2) * (2 * s[0] + (n - 1) * d)
    return ss - sum(s)

'''
extract file name
You have to extract a portion of the file name as follows:
Assume it will start with date represented as long number
Followed by an underscore
You'll have then a filename with an extension it will always have an extra extension at the end

Inputs:
1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION
1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34
1231231223123131_myFile.tar.gz2

Outputs:
FILE_NAME.EXTENSION
This_is_an_otherExample.mpg
myFile.tar
''' 
class FileNameExtractor:
    @staticmethod
    def extract_file_name(d):
        t = d.split("_")
        f = "_".join(t[1:])
        h = f.split(".")
        return ".".join(h[:2])

'''
Coding Meetup #7 - Higher-Order Functions Series - Find the most senior developer
You will be given a sequence of objects representing data about developers who have signed up to attend the next 
coding meetup that you are organising.
Your task is to return a sequence which includes the developer who is the oldest. 
In case of a tie, include all same-age senior developers listed in the same order as they appeared in the original input array.

For example, given the following input array:
list1 = [
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
  { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
your function should return the following array:
[
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
''' 
def find_senior(lst): 
    mx = 0
    fin = []
    for el in lst:
        if el['age'] > mx:
            mx = el['age']
    for el in lst:
        if el['age'] == mx:
            fin.append(el)
    return fin

'''
Format words into a sentence
Complete the method so that it formats the words into a single comma separated value. 
The last word should be separated by the word 'and' instead of a comma. 
The method takes in an array of strings and returns a single formatted string.

Note:
Empty string values should be ignored.
Empty arrays or null/nil/None values being passed into the method should result in an empty string being returned.
Example: (Input --> output)

['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
['ninja', '', 'ronin'] --> "ninja and ronin"
[] -->""
''' 
def format_words(words):
    fin = []
    if words == None: return ""
    for el in words:
        if el != "":
            fin.append(el)
    if len(fin) == 0:
        return ""
    elif len(fin) == 1:
        return fin[0]
    elif len(fin) == 2:
        return fin[0] + ' and ' + fin[1]
    else:
        return ", ".join(fin[:-1]) + ' and ' + fin[-1]

'''
Pascal's Triangle #2
Your function will be passed the depth of the triangle and your code has to return the corresponding Pascal's triangle up to that depth.

The triangle should be returned as a nested array. For example:

pascal(5) -> [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]
To build the triangle, start with a single 1 at the top, for each number 
in the next row you just take the two numbers above it and add them together, except for the edges, which are all 1. e.g.:

      1
    1   1
  1   2   1
1   3   3   1
''' 
def pascal(p):
    fin = []
    fin.append([1])
    if p == 1: return fin
    for i in range(1, p):
        fin.append(getRow(i))
    return fin
    
def getRow(n):
    prev = 1
    aux = []
    aux.append(1)
    for i in range(1, n + 1):
        curr = (prev * (n - i + 1)) // i
        aux.append(curr)
        prev = curr
    return aux    

'''
Coding Meetup #15 - Higher-Order Functions Series - Find the odd names
You will be given an array of objects representing data about developers who have signed 
up to attend the next coding meetup that you are organising.

Given the following input array:
var list1 = [
  { firstName: 'Aba', lastName: 'N.', country: 'Ghana', continent: 'Africa', age: 21, language: 'Python' },
  { firstName: 'Abb', lastName: 'O.', country: 'Israel', continent: 'Asia', age: 39, language: 'Java' }
];
write a function that when executed as findOddNames(list1) returns only the developers where if you add 
the ASCII representation of all characters in their first names, the result will be an odd number:

[{ firstName: 'Abb', lastName: 'O.', country: 'Israel', continent: 'Asia', age: 39, language: 'Java' }]

Explanation of the above:
Sum of ASCII codes of letters in 'Aba' is: 65 + 98 + 97 = 260 which is an even number
Sum of ASCII codes of letters in 'Abb' is: 65 + 98 + 98 = 261 which is an odd number
''' 
def find_odd_names(lst): 
    fin = []
    for el in lst:
        sum = 0
        for subel in el['firstName']:
            sum += ord(subel)
        if sum % 2 != 0: fin.append(el)
    return fin

'''
Simple Fun #135: Missing Alphabets
Given string s, which contains only letters from a to z in lowercase.

A set of alphabet is given by abcdefghijklmnopqrstuvwxyz.
2 sets of alphabets mean 2 or more alphabets.
Your task is to find the missing letter(s). You may need to output them by the order a-z. 
It is possible that there is more than one missing letter from more than one set of alphabet.

If the string contains all of the letters in the alphabet, return an empty string ""
Example
For s='abcdefghijklmnopqrstuvwxy'
The result should be 'z'
For s='aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy'
The result should be 'zz'
For s='abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy'
The result should be 'ayzz'
For s='codewars'
The result should be 'bfghijklmnpqtuvxyz'
Input/Output
[input] string s
Given string(s) contains one or more set of alphabets in lowercase.
[output] a string
Find the letters contained in each alphabet but not in the string(s). Output them by the order a-z. 
If missing alphabet is repeated, please repeat them like "bbccdd", not "bcdbcd"
''' 
def missing_alphabets(s):
    al = "abcdefghijklmnopqrstuvwxyz"
    max = 0
    fin = ''
    for el in set(s):
        if max < s.count(el): max = s.count(el)
    for el in al:
        fin += (max - s.count(el)) * el
    return fin

'''
Exclamation marks series #17: Put the exclamation marks and question marks on the balance - are they balanced?
Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings left and right on the balance - are they balanced?

If the left side is more heavy, return "Left"; if the right side is more heavy, return "Right"; if they are balanced, return "Balance".
Examples
"!!", "??"     -->  "Right"
"!??", "?!!"   -->  "Left"
"!?!!", "?!?"  -->  "Left"
"!!???!????", "??!!?!!!!!!!"  -->  "Balance"
''' 
def balance(left, right):
    sum1 = left.count("!") * 2 + left.count("?") * 3
    sum2 = right.count("!") * 2 + right.count("?") * 3
    if sum1 > sum2:
        return "Left"
    elif sum2 > sum1:
        return "Right"
    else:
        return "Balance"
  
'''
Remember
Write a function that takes a string and returns an array of the repeated characters (letters, numbers, whitespace) in the string.
If a charater is repeated more than once, only show it once in the result array.
Characters should be shown by the order of their first repetition. 
Note that this may be different from the order of first appearance of the character.

Characters are case sensitive.
For F# return a "char list"

Examples:
remember("apple") => returns ["p"]
remember("apPle") => returns []          # no repeats, "p" != "P"
remember("pippi") => returns ["p","i"]   # show "p" only once
remember('Pippi') => returns ["p","i"]   # "p" is repeated first
'''
def remember(s):
    l = len(s)
    iter = 0
    fin = []
    while iter <= l:
        newS = s[:iter]
        for el in set(newS):
            if newS.count(el) > 1:
                if el not in fin:
                    fin.append(el)
        iter += 1
    return fin

'''
Are we alternate?
Create a function isAlt() that accepts a string as an argument and validates 
whether the vowels (a, e, i, o, u) and consonants are in alternate order.

is_alt("amazon")  # True
is_alt("apple")   # False
is_alt("banana")  # True
Arguments consist of only lowercase letters.
'''
def is_alt(s):
    if s[0] in 'aeiou':
        for i in range(1, len(s), 2):
            if s[i] in 'aeiou':
                return False
        for i in range(0, len(s), 2):
            if s[i] not in 'aeiou':
                return False
    else:
        for i in range(0, len(s), 2):
            if s[i] in 'aeiou':
                return False
        for i in range(1, len(s), 2):
            if s[i] not in 'aeiou':
                return False
    return True

'''
Coding Meetup #13 - Higher-Order Functions Series - Is the meetup language-diverse?
You will be given an array of objects representing data about developers who have signed up to attend the 
next web development meetup that you are organising. Three programming languages will be represented: Python, Ruby and JavaScript.

Your task is to return either:
true if the number of meetup participants representing any of the three programming languages is ** at most 2 times 
higher than the number of developers representing any of the remaining programming languages**; or
false otherwise.
For example, given the following input array:
list1 = [
    { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'Python' },
    { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'Ruby' },
    { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 43, 'language': 'Ruby' },
    { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 95, 'language': 'JavaScript' },
    { 'firstName': 'Jayden', 'lastName': 'P.', 'country': 'Jamaica', 'continent': 'Americas', 'age': 18, 'language': 'JavaScript' },
    { 'firstName': 'Joao', 'lastName': 'D.', 'country': 'Portugal', 'continent': 'Europe', 'age': 25, 'language': 'JavaScript' }
    ]
your function should return false as the number of JavaScript developers (3) is 3 
times higher than the number of Python developers (1). It can't be more than 2 times higher to be regarded as language-diverse.
'''
def is_language_diverse(lst): 
    fin = []
    for el in lst:
        fin.append(el['language'])
    js, rb, py = 0, 0, 0
    js = fin.count("JavaScript")
    rb = fin.count("Ruby")
    py = fin.count("Python")
    if min(js, rb, py) * 2 < max(js, rb, py):
        return False
    return True

'''
Single character palindromes
You will be given a string and you task is to check if it is possible to convert that string into a palindrome 
by removing a single character. If the string is already a palindrome, return "OK". If it is not, and we can convert it 
to a palindrome by removing one character, then return "remove one", otherwise return "not possible". 
The order of the characters should not be changed.

For example:
solve("abba") = "OK". -- This is a palindrome
solve("abbaa") = "remove one". -- remove the 'a' at the extreme right. 
solve("abbaab") = "not possible". 
'''
def solve(s):
    if s == s[::-1]: return 'OK'
    for i in range(0, len(s)):
        fin = list(s)
        fin.pop(i)
        aux = "".join(fin)
        if aux == aux[::-1]: return 'remove one'
    return 'not possible'

'''
Roman Numerals Encoder
Create a function taking a positive integer between 1 and 3999 (both included) as its parameter 
and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with 
the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 
1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each 
Roman symbol in descending order: MDCLXVI.

Example:
solution(1000) # should return 'M'
Help:
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
Remember that there can't be more than 3 identical symbols in a row.
'''
def solution(num):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]

    ans = (thousands + hundreds + tens + ones)

    return ans

'''
The takeWhile Function
Here's another staple for the functional programmer. You have a sequence of values and some predicate for those values.
You want to get the longest prefix of elements such that the predicate is true for each element. 
We'll call this the takeWhile function. It accepts two arguments. 
The first is the sequence of values, and the second is the predicate function. 
The function does not change the value of the original sequence.

Example:
sequence : [2,4,6,8,1,2,5,4,3,2]
predicate: is an even number
result   : [2,4,6,8]
Your task is to implement the takeWhile function.
'''
def take_while(a, p):
    fin = []
    for el in a:
        if p(el):
            fin.append(el)
        else:
            return fin
    return fin

'''
Coding Meetup #9 - Higher-Order Functions Series - Is the meetup age-diverse?
You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed 
up to attend the next coding meetup that you are organising.

Your task is to return:
true if developers from all of the following age groups have signed up: teens, twenties, thirties, forties, fifties, sixties,
seventies, eighties, nineties, centenarian (at least 100 years young).
false otherwise.
For example, given the following input array:

list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 29, 'language': 'JavaScript' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 40, 'language': 'Ruby' },
  { 'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 59, 'language': 'C' },
  { 'firstName': 'Maria', 'lastName': 'S.', 'country': 'Peru', 'continent': 'Americas', 'age': 60, 'language': 'C' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 75, 'language': 'Python' },
  { 'firstName': 'Chloe', 'lastName': 'K.', 'country': 'Guernsey', 'continent': 'Europe', 'age': 88, 'language': 'Ruby' },
  { 'firstName': 'Viktoria', 'lastName': 'W.', 'country': 'Bulgaria', 'continent': 'Europe', 'age': 98, 'language': 'PHP' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript' }
]
your function should return true as there is at least one developer from each age group.

Notes:
The input array will always be valid and formatted as in the example above.
Age is represented by a number which can be any positive integer up to 199.
'''   
def is_age_diverse(lst): 
    fin = []
    for el in lst:
        x = el['age']//10
        if x >=10: x = 10
        if x !=0: fin.append(x)
    print(list(set(fin)))
    return True if list(set(fin)) == [x for x in range(1, 11)] else False

'''
Give me a Diamond
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. 
Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a 
diamond of even or negative size.

Examples
A size 3 diamond:

 *
***
 *
...which would appear as a string of " *\n***\n *\n"

A size 5 diamond:

  *
 ***
*****
 ***
  *
...that is:

"  *\n ***\n*****\n ***\n  *\n"
'''  
def diamond(n):
    top, bot = [], []
    if n < 1 or n % 2 == 0: return None
    t, b =  n // 2 + 1, n // 2
    es = b
    j = 0
    for i in range(1, t + 1):
        top.append(es * ' ' + (i + j) * '*' + '\n')
        j += 1
        es -= 1
    j = 0
    es = b
    for i in range(1, b + 1):
        bot.append(es * ' ' + (i + j) * '*' + '\n')
        j += 1
        es -= 1
    return "".join(top) + "".join(bot[::-1])

'''
Coding Meetup #8 - Higher-Order Functions Series - Will all continents be represented?
You will be given a sequence of objects (associative arrays in PHP) representing data about developers who have 
signed up to attend the next coding meetup that you are organising.

Your task is to return:
true if all of the following continents / geographic zones will be represented by at least one 
developer: 'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
false otherwise.
For example, given the following input array:

list1 =  [
  { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
  { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
  { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
  ]
your function should return true as there is at least one developer from the required 5 geographic zones.

Notes:
The input array and continent names will always be valid and formatted as in the list above for example 'Africa' will
always start with upper-case 'A'.
'''  
def all_continents(lst): 
    fin = []
    for el in lst:
        fin.append(el['continent'])
    return True if len(set(fin)) == 5 else False

'''
Simple Encryption #1 - Alternating Split
Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with 
all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
'''  
def decrypt(text, n):
    if n <= 0 or text == None: 
        return text
    else:
        new = []
        l = len(text)//2
        f = text[l:]
        s = text[:l]
        for i in range(l + 1):
            try:
                new.append(f[i])
            except:
                pass
            try:
                new.append(s[i])
            except:
                pass
        n -= 1
        return decrypt("".join(new), n)
    
'''
String transformer
Given a string, return a new string that has transformed based on the input:

Change case of every character, ie. lower case to upper case, upper case to lower case.
Reverse the order of words from the input.
Note: You will have to handle multiple spaces, and leading/trailing spaces.

For example:

"Example Input" ==> "iNPUT eXAMPLE"
You may assume the input only contain English alphabet and spaces.
'''
def string_transformer(s):
    fin = []
    l = s.split(" ")
    for word in l:
        new = ''
        for let in word:
            if let.isupper():
                new += let.lower()
            else:
                new += let.upper()
        fin.append(new)
    return " ".join(fin[::-1])

'''
IP Validation
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
'''
def is_valid_IP(s):
    l = s.split(".")
    i = 0
    for el in l:
        try: 
            if str(int(el)) == el:
                if 0 <= int(el) <= 255:
                    i += 1
                    pass
        except:
            return False
    return True if i == 4 else False
   
'''
Sum two arrays
Your task is to create a function called sum_arrays(), which takes two arrays consisting of integers, 
and returns the sum of those two arrays.

The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9, it would equal '3' + '2' + '9' 
converted to an integer for this kata, meaning it would equal 329. The output should be an array of the sum in 
a similar fashion to the input (for example, if the sum is 341, you would return [3,4,1]). 
Examples are given below of what two arrays should return.

[3,2,9],[1,2] --> [3,4,1]
[4,7,3],[1,2,3] --> [5,9,6]
[1],[5,7,6] --> [5,7,7]
If both arrays are empty, return an empty array.
In some cases, there will be an array containing a negative number as the first index in the array. 
In this case treat the whole number as a negative number. See below:
[3,2,6,6],[-7,2,2,8] --> [-3,9,6,2] # 3266 + (-7228) = -3962
'''
def sum_arrays(a1,a2):
    flag = False
    if a1 == [] and a2 == []: return []
    num1 = "".join([str(x) for x in a1])
    num2 = "".join([str(x) for x in a2])
    if num1 == '': num1 = '0'
    if num2 == '': num2 = '0'
    a3 = int(num1) + int(num2)
    if a3 < 0: 
        flag = True
        a3 *= -1
    a4 = [int(x) for x in str(a3)]
    if flag: a4[0] = a4[0] * -1
    return a4
    
'''
Triangle type
In this kata, you should calculate type of triangle with three given sides a, b and c (given in any order).
If all angles are less than 90°, this triangle is acute and function should return 1.
If one angle is strictly 90°, this triangle is right and function should return 2.
If one angle more than 90°, this triangle is obtuse and function should return 3.
If three sides cannot form triangle, or one angle is 180° (which turns triangle into segment) - function should return 0.
Input parameters are sides of given triangle. All input values are non-negative floating point or integer numbers (or both).

Examples:
triangle_type(2, 4, 6) # return 0 (Not triangle)
triangle_type(8, 5, 7) # return 1 (Acute, angles are approx. 82°, 38° and 60°)
triangle_type(3, 4, 5) # return 2 (Right, angles are approx. 37°, 53° and exactly 90°)
triangle_type(7, 12, 8) # return 3 (Obtuse, angles are approx. 34°, 106° and 40°)
'''
def triangle_type(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        n = sorted([a, b, c])
        ty =  n[0] ** 2 + n[1] ** 2
        if ty < n[2] ** 2: 
            return 3
        elif ty == n[2] ** 2:
            return 2
        else:
            return 1
    else:
        return 0
