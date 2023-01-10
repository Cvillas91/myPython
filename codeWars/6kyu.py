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
