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
