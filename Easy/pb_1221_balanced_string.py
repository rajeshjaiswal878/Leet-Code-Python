import time

# Questions Details:
'''
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Problem Link:https://leetcode.com/problems/split-a-string-in-balanced-strings/
'''


# My Solution
def my_balanced_string_split(s):
    l, r = 0, 0
    for ch in s:
        l += 1 if ch == 'L' else -1
        r += l == 0
    return r


# Leet Code Best Solution
def balancedStringSplit(s):
    res = 0
    rc, lc = 0, 0
    for char in s:
        if char == 'R':
            rc += 1
        else:
            lc += 1
        if rc == lc:
            rc, lc = 0, 0
            res += 1
    return res


# Function/ Method Call and Time CalCulation Set
print('----All Methods Time Calculation----')
s = "RLRRLLRLRL"
func_name = my_balanced_string_split.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = my_balanced_string_split(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

func_name = balancedStringSplit.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = balancedStringSplit(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

'''
Output



'''
