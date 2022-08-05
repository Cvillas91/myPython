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
