import re

def find_sequences(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)

sequence = find_sequences("a_b_c_d_e_f")
for seq in sequence:
    print (seq)