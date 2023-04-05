'''
A format for expressing an ordered list of integers is to use a comma separated list of either individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. 
For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a 
correctly formatted string in the range format.

Example:
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
'''
def solution(args):
    fin = [args[0]]
    dest = ''
    for i in range(1, len(args)):
        if args[i] - 1 in args and args[i] + 1 in args:
            pass
        else:
            fin.append(args[i])
    
    for el in fin:
        if el + 1 in fin:
            dest += str(el) + ','
        elif el + 1 not in args:
            dest += str(el) + ','
        else:
            dest += str(el) + '-'
    
    return dest[:-1]
            
'''
Most frequently used words in a text
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, 
in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
'''
def top_3_words(text):
    df = {}
    text = text.replace(",", " ").replace("/", " ").replace("#", " ").replace(".", " ").replace("\n", " ").replace(":", " ")
    text = text.replace(";", " ").replace("!", " ").replace("?", " ").replace("-", " ").replace("_", " ").lower()
    new = sorted(text.split(" "))
    st = set(new)
    for el in st:
        if el != '':
            df[el] =  new.count(el)
    if len(df) > 1:
        for el in df:
            if not any(c.isalpha() for c in el):
                del df[el]
    else:
        for el in df:
            if not any(c.isalpha() for c in el):
                return []
    if len(df) >= 3:
        t1v = [x for x in df if df[x] == df[max(df, key=df.get)]]
        top1 = sorted(t1v, key=str.swapcase)[0]
        del df[top1]
        t2v = [x for x in df if df[x] == df[max(df, key=df.get)]]
        top2 = sorted(t2v, key=str.swapcase)[0]
        del df[top2]
        t3v = [x for x in df if df[x] == df[max(df, key=df.get)]]
        top3 = sorted(t3v, key=str.swapcase)[0]
        del df[top3]
        return [top1, top2, top3]
    elif len(df) >= 2:
        t1v = [x for x in df if df[x] == df[max(df, key=df.get)]]
        top1 = sorted(t1v, key=str.swapcase)[0]
        del df[top1]
        t2v = [x for x in df if df[x] == df[max(df, key=df.get)]]
        top2 = sorted(t2v, key=str.swapcase)[0]
        del df[top2]
        return [top1, top2]
    elif len(df) >= 1:
        t1v = [x for x in df if df[x] == df[max(df, key=df.get)]]
        top1 = sorted(t1v, key=str.swapcase)[0]
        del df[top1]
        return [top1]
    else:
        return []
