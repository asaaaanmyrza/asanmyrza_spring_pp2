
import time
import math

def all_true(tuple_data):
    return all(tuple_data)


tuple1 = (True, True, True)
tuple2 = (True, False, True)
print(all_true(tuple1))  
print(all_true(tuple2))  