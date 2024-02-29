import re

def match_pattern(string):
    pattern = r'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

print(match_pattern("acb"))