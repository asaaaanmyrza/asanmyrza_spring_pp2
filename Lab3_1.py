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

#






#



#



#



#



#






#



#



#



#



#






#



#



#



#



#






#



#



#



#



#






#



#



#



#



#






#



#



#



#



#






#



#



#



#



#







