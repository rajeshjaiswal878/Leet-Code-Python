from string import ascii_lowercase
from icecream import ic
import time

# Questions Details:
'''
You are given a string allowed consisting of distinct 
characters and an array of strings words. 
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since 
they only contain characters 'a' and 'b'.

Problem Link:https://leetcode.com/problems/count-the-number-of-consistent-strings/
'''


# My Solution
def my_count_consisting(allowed, words):
    count = 0
    sll_set = set(allowed)

    for word in words:
        if set(word).issubset(set(allowed)):
            count += 1
        else:
            continue
    return count


# Leet Code Best Solution
def countConsistentStrings_best(allowed, words):
    return sum(map((set(ascii_lowercase) - set(allowed)).isdisjoint, words))


# Leet Code 2nd Best Solution
def countConsistentStrings(allowed, words):
    return sum(map(set(allowed).issuperset, words))


# Function/ Method Call and Time CalCulation Set
print('----All Methods Time Calculation----')
allowed = 'ab'
words = ["ad", "bd", "aaab", "baa", "badab"]
func_name = my_count_consisting.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = my_count_consisting(allowed, words)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

func_name = countConsistentStrings_best.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = countConsistentStrings_best(allowed, words)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

func_name = countConsistentStrings.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = countConsistentStrings(allowed, words)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

'''
Output
----All Methods Time Calculation----
Result : 2 of Method: My Count Consisting Took 7.152557373046875e-06 Time
----------------------------------------
Result : 2 of Method: Countconsistentstrings Best Took 6.890296936035156e-05 Time
----------------------------------------
Result : 2 of Method: Countconsistentstrings Took 6.198883056640625e-06 Time
----------------------------------------
'''
