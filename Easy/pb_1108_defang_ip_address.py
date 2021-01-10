import time

'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Problem Link:  https://leetcode.com/problems/defanging-an-ip-address/
'''


# My Solution:

def defang_ip_address(s):
    return s.replace('.', '[.]')


# Leet Code Best Solution
def defangIPaddr(address):
    return '[.]'.join(address.split('.'))


print('----All Methods Time Calculation----')
s = '1.1.1.1'
func_name = defang_ip_address.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = defang_ip_address(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

s = '1.1.1.1'
func_name = defangIPaddr.__name__
func_name = func_name.replace('_', ' ').title()
tic = time.time()
res = defangIPaddr(s)
toc = time.time()
print(f'Result : {res} of Method: {func_name} Took {toc - tic} Time')
print('--' * 20)

''' 
Output
----All Methods Time Calculation----
Result : 1[.]1[.]1[.]1 of Method: Defang Ip Address Took 9.5367431640625e-07 Time
----------------------------------------
Result : 1[.]1[.]1[.]1 of Method: Defangipaddr Took 2.1457672119140625e-06 Time
----------------------------------------

'''
