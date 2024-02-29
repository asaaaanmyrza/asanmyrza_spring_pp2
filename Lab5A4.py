import re

def find_sequences(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

sequence = find_sequences("AaaAsd")
for seq in sequence:
    print (seq)