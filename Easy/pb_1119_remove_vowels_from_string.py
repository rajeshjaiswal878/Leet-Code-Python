'''
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:
Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:
Input: s = "aeiou"
Output: ""

Problem Line:https://leetcode.com/problems/remove-vowels-from-a-string/
'''

import time


def remove_vowels_from_string(s):
    res = [ch for ch in s if ch not in 'aieou']
    return ''.join(res)


def removeVowels(s):
    v = set('aeiou')
    return ''.join(i for i in s if i not in v)


def removeVowels_most_favored(s):
    vowels = set("aeiou")
    lst = list(s)
    # create two points at the start and end
    p1, p2 = 0, len(lst) - 1

    # loop the string list
    while p1 <= p2:
        if lst[p1] in vowels:
            lst[p1] = ""
        if lst[p2] in vowels:
            lst[p2] = ""
        p1 += 1
        p2 -= 1
    return "".join(lst)


print('--' * 30)
print('----All Methods Time Calculation----')

s = 'aeiou'
func_name = remove_vowels_from_string.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = removeVowels_most_favored(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

func_name = removeVowels.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = removeVowels(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

func_name = removeVowels_most_favored.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = removeVowels_most_favored(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

''' 
Output:

------------------------------------------------------------
----All Methods Time Calculation----
Result :  of Method: Remove Vowels From String Took 1.7881393432617188e-05 Time
----------------------------------------
Result :  of Method: Removevowels Took 3.814697265625e-06 Time
----------------------------------------
Result :  of Method: Removevowels Most Favored Took 2.1457672119140625e-06 Time
----------------------------------------
'''
