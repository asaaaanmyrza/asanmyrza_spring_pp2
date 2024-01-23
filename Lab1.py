## Syntax 1

print('Hello World')

## 2

if(5>2):
    print('YES')

## Comments 1
    
#This is a comment
    
##  2

""" 
This is a comment
written in 
more than just one line
"""

## Variables 1

carname = 'Volvo'

## 2

x = 50

## 3

x = 5
y = 10
print(x + y)

## 4

x = 5
y = 10
z = x + y
print(z)

## 5

x, y, z = "Orange", "Banana", "Cherry"

## 6

x = y = z = 'Orange'

## 7

def myfunc():
  global x 
  x = "fantastic"

## Data types 1

int (10)

## 2

str ('Hello World!')

## 3

float (10.5)

## 4

list (['apple', 'banana', 'lemon']) #Простой список, изменяемый

## 5

tuple (('apple', 'banana', 'lemon')) #Закрытый список, неизменяемый

## 6

dict ({"name" : "John", "age" : 36}) #Список где у каждого элемента имеется индивидуальный ключ

## 7

bool (True) #Логическое отрицание или подтверждение

## Numbers 1

x = 5
x = float(x)

## 2

x = 5.5
x = int(x)

## 3

x = 5
x = complex(x)

## Strings 1

x=('Hello World!')
print(len(x))

## 2

txt = "Hello World"
x = txt[0]

## 3

txt = "Hello World"
x = txt[2:5] ## от второго индекса до четвертого, пятый не в счет

## 4

txt = "Hello World"
x = txt.strip()

## 5

txt = "Hello World"
x = txt.upper()

