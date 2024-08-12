##1. define a function and iterable(i.e, a list ), use them in map
##2. define a function and iterable, use that and filter items
##3. define a function for reduce from functools module, and use them to find the largest value
##4. create a module and import and use them in another file
##5. import math module and run sqrt, ceil, floor and pi with proper explanation in comment line


##1. define a function and iterable(i.e, a list ), use them in map
l=[1,2,3,4,5,6,7,8,9]
def square(x):
    return x**2
print(list(map(square,l)))
    
print("---------------------------------------------------")


##2. define a function and iterable, use that and filter items
age=[12,13,18,47,45,78]
def my(x):
    if x>=18:
        return True
    else :
        return False

adult = filter(my,age)

for x in adult:
    print(x)
print("---------------------------------------------------")

##3. define a function for reduce from functools module, and use them to find the largest value
import functools
l=[1,2,3,4,5,6,7,8,9]

print(functools.reduce(lambda x,y :x if x>y else y ,l))


##4. create a module and import and use them in another file

import module

module.hello("lingesh")
