
import time
import math

def is_palindrome(s):
    return s == s[::-1]


input_string = input()
if is_palindrome(input_string):
    print("True")
else:
    print("False")
