import time

# Questions Details:
'''
You are given a string s of even length. Split this string into two 
halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels 
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.


Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel.
 Therefore, they are alike.

Problem Link:https://leetcode.com/problems/determine-if-string-halves-are-alike/
'''


# My Solution
def my_halvesAreAlike(s):
    mid = int(len(s) / 2)
    a = [ch for ch in s[:mid] if ch in 'aeiouAEIOU']
    b = [ch for ch in s[mid:] if ch in 'aeiouAEIOU']
    if len(a) == len(b):
        return True
    return False


# Leet Code Best Solution
def X(s):
    l, r = 0, len(s) - 1
    count = 0
    vowels = set(['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'])
    while l < r:
        if s[l] in vowels:
            count += 1
        if s[r] in vowels:
            count -= 1
        l += 1
        r -= 1
    return count == 0


# Function/ Method Call and Time CalCulation Set
print('----All Methods Time Calculation----')
s = 'AbCdEfGh'
func_name = my_halvesAreAlike.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = my_halvesAreAlike(s)
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
