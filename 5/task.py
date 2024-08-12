##convert a string to dictionary and len as its value

user=input("enter a word:")
dict={user:len(user)}
print(dict)

##find the length of a string with out using len function

def length (s):
    count=0
    for i in s:
        count+=1
    return count 
user=input("enter a word:")
j = length (user)
print(j)
    
##remove white space from the string
user=input("enter a word:")
join = user.replace(" " ,"")
print(join)


####my=("ling","esh")
##x="".join(my)
##print(x)


##reserve a srting without using slicing method

user=input("enter a word:")
user=list(user)
user.reverse()
user="".join(user)
print(user)


##1. define a function to convert temperature to fahrenheit
##2. define a calculator function (e.g format, def calculator(a, b, operation( +/-/*,etc )))
##3. create a function for rolling a dice, when we call the function,it should randomly generate a number between 1 and 6
##4. find the area of the circle (use math module) define function!

##1. define a function to convert temperature to fahrenheit
def temperature (user):
    f=(user*9/5)+32
    return f
user = int(input("enter a number:"))
print(temperature(user),"F")
    

##2. define a calculator function (e.g format, def calculator(a, b, operation( +/-/*,etc )))
def calculator (a,b,operator):
    if operator == "+":
        return a+ b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    else:
        return "error pls use (+,-,*)"
print(calculator(2,5,"*"))


##3. create a function for rolling a dice, when we call the function,it should randomly generate a number between 1 and 6
import random

dice=[1,2,3,4,5,6]
rolle_dice=random.choice(dice)
print(rolle_dice)

##4. find the area of the circle (use math module) define function!
import math
from math import *
def area_of(a):
    return pi*(a**2)
user= int(input("enter a number:"))
print(area_of(user))
