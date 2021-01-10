import time

# from icecream import ic

# Questions Details:
'''
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating 
the layout of the keyboard (indexed from 0 to 25), 
initially your finger is at index 0. To type a character, 
you have to move your finger to the index of the desired character. 
The time taken to move your finger from index i to index j is |i - j|.
You want to type a string word. Write a function to calculate
how much time it takes to type it with one finger.
Example 1:

Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4. 


Problem Link:https://leetcode.com/problems/single-row-keyboard/submissions/
'''


# My Solution

def single_row_key_board(keyboard, s):
    ch = [ch for ch in keyboard]
    map = {ch[i]: i for i in range(26)}
    res = 0
    for i in range(len(s)):
        if i == 0:
            res = abs(map.get(s[i]) - res)
        else:
            '''ic(s[i])
            ic(map.get(s[i - 1]))
            ic(map.get(s[i]))
            diff = abs(map.get(s[i - 1]) - map.get(s[i]))
            ic(diff)'''
            res = res + abs(map.get(s[i - 1]) - map.get(s[i]))

    return res


def calculateTime(kbd, w):
    c2pos = {c: i for i, c in enumerate(kbd)}
    i = 0
    cost = 0
    for c in w:
        j = c2pos[c]
        cost += abs(j - i)
        i = j
    return cost


# Function/ Method Call and Time CalCulation Set
print('----All Methods Time Calculation----')
keyboard = 'pqrstuvwxyzabcdefghijklmno'
s = 'leetcode'
func_name = single_row_key_board.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = single_row_key_board(keyboard, s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

func_name = calculateTime.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = calculateTime(keyboard, s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

'''
Output

----All Methods Time Calculation----
Result : 73 of Method: Single Row Key Board Took 1.4066696166992188e-05 Time
----------------------------------------
Result : 73 of Method: Calculatettime Took 6.9141387939453125e-06 Time
----------------------------------------
'''
