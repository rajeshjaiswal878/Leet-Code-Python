import time

# Questions Details:
'''
A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's 
(with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.
Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Problem Link:https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
'''


# My Solution
def my_max_nest_depth(s):
    l = 0
    max_depth = 0
    for ch in s:
        if ch == '(':
            l += 1
        elif ch == ')':
            max_depth = max(max_depth, l)
            l -= 1
    return max_depth


# Leet Code Best Solution
def maxDepth(s):
    max_depth = 0
    current_depth = 0
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1
    return max_depth


# Function/ Method Call and Time CalCulation Set
print('----All Methods Time Calculation----')
s = "(1+(2*3)+((8)/4))+1"
func_name = my_max_nest_depth.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = my_max_nest_depth(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

func_name = maxDepth.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = maxDepth(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

'''
Output
----All Methods Time Calculation----
Result : 3 of Method: My Max Nest Depth Took 5.0067901611328125e-06 Time
----------------------------------------
Result : 3 of Method: Maxdepth Took 4.0531158447265625e-06 Time
----------------------------------------

'''
