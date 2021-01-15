import string

import time

# Questions Details:
'''
Implement function ToLowerCase() that has a string parameter str, 
and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"

Problem Link:https://leetcode.com/problems/to-lower-case/
'''


# My Solution
def my_lowercase_without_lower_function(s):
    upp = [ch for ch in string.ascii_uppercase]
    low = [ch for ch in string.ascii_lowercase]
    mapp = {upp[i]: low[i] for i in range(len(upp))}
    res = ''
    for ch in s:
        if ch in mapp:
            res = res + mapp.get(ch)
        else:
            res = res + ch
    return res


def my_lower_case_with_lower_function(s):
    print(s.lower())


# Leet Code Best Solution
def toLowerCase(s):
    result = ""
    for i in s:
        if i.isalpha() and i.islower() == False:
            result += chr(ord(i) + 32)
        else:
            result += i
    return result


# Function/ Method Call and Time CalCulation Set
print('----All Methods Time Calculation----')
s = 'Rajesh'
func_name = my_lowercase_without_lower_function.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = my_lowercase_without_lower_function(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

my_lower_case_with_lower_function(s)
print('--' * 20)

func_name = toLowerCase.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = toLowerCase(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

'''
Output
----All Methods Time Calculation----
Result : rajesh of Method: My Lowercase Without Lower Function Took 1.5020370483398438e-05 Time
----------------------------------------
rajesh
----------------------------------------
Result : rajesh of Method: Tolowercase Took 8.821487426757812e-06 Time
----------------------------------------
'''
