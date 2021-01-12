import time

# Questions Details:
'''
You own a Goal Parser that can interpret a string command. 
The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", 
"()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Problem Link: https://leetcode.com/problems/goal-parser-interpretation/
'''


# My Solution

def goal_parser_interpreter(s):
    return s.replace('()', 'o').replace('(al)', 'al')


def interpret(command):
    d = {'G': 'G', '()': 'o', '(al)': 'al'}
    prev = ''
    ans = ''
    for i in range(len(command)):
        prev = prev + command[i]
        if d.get(prev, False):
            ans = ans + d.get(prev)
            prev = ''
    return ans


# Function/ Method Call and Time CalCulation Set
print('----All Methods Time Calculation----')
s = 'G()()()()(al)'
func_name = goal_parser_interpreter.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = goal_parser_interpreter(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

print('----All Methods Time Calculation----')
s = 'G()()()()(al)'
func_name = interpret.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = interpret(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

'''
Output

----All Methods Time Calculation----
Result : Gooooal of Method: Goal Parser Interpreter Took 1.9073486328125e-06 Time
----------------------------------------
----All Methods Time Calculation----
Result : Gooooal of Method: Interpret Took 6.198883056640625e-06 Time
----------------------------------------
'''
