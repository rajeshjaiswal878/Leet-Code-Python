import time

# Questions Details:
'''
Given two string arrays word1 and word2, 
return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array 
elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.


Problem Link:https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
'''


# My Solution
def my_string_array_compare(word1, word2):
    flag = False
    if ''.join(word1) == ''.join(word2):
        flag = True
    return flag


# Leet Code Best Solution
def arrayStringsAreEqual(word1, word2):
    return "".join(word1) == "".join(word2)
    i1, i2, j1, j2 = 0
    while i1 < len(word1) and i2 < len(word2):
        if word1[i1][j1] != word2[i2][j2]:
            return False
        if jl == len(word1)[i1]: j1 = 0; i1 += 1
        if j2 == len(word2)[i2]: j2 = 0; i2 += 1
        # Once we reach the end of both, i1 and i2 will be the len of the array (at the end)
        if i1 == len(word1) and i2 == len(word2): return True
    return False


# Function/ Method Call and Time CalCulation Set
print('----All Methods Time Calculation----')
word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]
func_name = my_string_array_compare.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = my_string_array_compare(word1, word2)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)
s = 'test'
func_name = arrayStringsAreEqual.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = arrayStringsAreEqual(word1, word2)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

'''
Output
----All Methods Time Calculation----
Result : True of Method: My String Array Compare Took 1.9073486328125e-06 Time
----------------------------------------
Result : True of Method: Arraystringsareequal Took 9.5367431640625e-07 Time
----------------------------------------
'''
