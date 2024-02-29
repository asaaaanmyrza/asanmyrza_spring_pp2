import re

def two_to_three(string):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False
    
print(two_to_three("abbbb"))