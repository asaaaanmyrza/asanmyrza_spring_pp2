
import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    print("Square root of", number, "after", milliseconds, "milliseconds is", result)


square_root_after_milliseconds(25100, 2123)
