# Functions 

# 1

print("Task 1")
def gramtoounce(weight):
    print(weight*28.3495231)
gramtoounce(5)
print(" ")
# 2

print("Task 2")
def ECT(faren):
    print(((faren - 32)/9)*5)
ECT(270)
print(" ")
# 3

print("Task 3")
def solve(numheads, numlegs):
    animals={"Chickens":0, "Rabbits":0}
    animals["Chickens"]=numlegs/2
    if(animals["Chickens"]>numheads):
        extraheads=animals["Chickens"]-numheads
        animals["Chickens"]-=extraheads
        animals["Rabbits"]=extraheads
    print("Chickens: ", animals["Chickens"],  " Rabbits: ", animals["Rabbits"])
solve(34, 94)
print(" ")

# 4

print("Task 4")

print(" ")

# 5

print("Task 5")

print(" ")

# 6

print("Task 6")

print(" ")

# 7

print("Task 7")
def has_33(nums):
    statement = False
    for i in range(0,len(nums)-1):
        if(nums[i] == 3 and nums[i+1] == 3):
            statement=True
            break
    return statement
print(has_33([3, 1, 3, 3]))

print(" ")

# 8

print("Task 8")
def has_007(nums):
    statement = False
    clone_nums=[]
    for i in range(0,len(nums)):
        if(nums[i]==0 or nums[i]==7):
            clone_nums.append(nums[i])
    for i in range(0,len(clone_nums)-2):
        if(clone_nums[i]==0 and clone_nums[i+1]==0 and clone_nums[i+2]==7):
            statement = True
            break
    return statement
print(has_007([0, 1, 5, 0, 0, 0, 7, 7, 0]))
print(" ")

# 9

print("Task 9")

import math
def vol(r):
    return 4/3 * math.pi * r *r *r
def square(r):
    return 4 * math.pi * r *r


print("Volume: ", vol(5))
print("Square: ", square(5))
print(" ")

# 10

print("Task 10")
def unique(lisst):
    lissst=[]
    lisst.sort()
    for i in range(0,len(lisst)-1):
        if(lisst[i]!=lisst[i+1]):
            lissst.append(lisst[i])
    lissst.append(lisst[len(lisst)-1])
    return lissst
print(unique([1, 1, 1, 1, 1, 1]))
print(" ")

# 11

print("Task 11")
def palindrome(word):
    result = True
    for i in range(0,int(len(word)/2)):
        if(word[i]!=word[len(word)-1-i]):
            result = False
            break
    return result
print(palindrome("aaaanaaaa"))
print(" ")

# 12

print("Task 12")
def histogram(nums):
    stars = ""
    for i in range(0,len(nums)):
        for j in range(0,nums[i]):
            stars = stars + "*"
        print(stars)
        stars=""
histogram([3, 10, 20])
print(" ")

# 14

print("Task 14")

print(" ")