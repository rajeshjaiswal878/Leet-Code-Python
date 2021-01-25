import time

# Questions Details:
'''
Given a string S, return the number of substrings that have only one distinct letter.

 

Example 1:

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: S = "aaaaaaaaaa"
Output: 55
Problem Link:https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/
'''


# My Solution

def my_countLetters(s):
    total = left = 0
    for right in range(len(s) + 1):
        if right == len(s) or s[left] != s[right]:
            len_substring = right - left
            total += (1 + len_substring) * len_substring // 2
            left = right
    return total


# Leet Code Best Solution
def X(s):
    total = 1
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            count = 1
        total += count
    return total


# Function/ Method Call and Time CalCulation Set
print('----All Methods Time Calculation----')
s = 'aaaba'
func_name = my_countLetters.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = my_countLetters(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

func_name = X.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = X(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

'''
Output



'''
