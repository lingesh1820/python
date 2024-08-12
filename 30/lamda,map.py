##local varible 

##def suma():
##    x="lingeshwar"
##    print(x)    
##suma()
##
####global 
##y="sakthivel"
##def suma():
##    global x
##    x="lingeshwar"
##    print(x+y)    
##suma()
##
##
####lambda
####syntax = lambda  argument :expersion
##
##m = lambda x,y,z : x*y*z
##
##print(m(20,40,50))
##




###local variable and global variable
##1. assign a variable inside the function and print outside the function
##2. modify a global variable using a function
##
###lambda function
##1. create a lambda function to multiply two arguments
##2. create a lambda function to add two arguments
##3. create a lambda function to subtract two arguments
##
### lambda + map function
##
##1. find the squares of the elements inside the list
##2. subtract 1 from all the elements inside the list
##3. find the len of the strings present inside the list



##1. assign a variable inside the function and print outside the function
def fun():
    z="lingeshwar"
    x="sakthivel"
    print(z+x)
fun()
print()


##2. modify a global variable using a function
def fun(): 
    global x,z
    z="lingeshwar"
    x="sakthivel"
fun()
print(z+x)

print("----------------------------------------")

##1. create a lambda function to multiply two arguments
m=lambda x,y : x*y
print(m(20,40))

##2. create a lambda function to add two arguments
a=lambda x,y : x+y
print(a(20,40))

##3. create a lambda function to subtract two arguments
s=lambda x,y : x-y
print(s(20,40))

print("----------------------------------------")

##1. find the squares of the elements inside the list
l=[1,2,3,4,590,80,90]
def square(u):
    return u**2
print(list(map(square ,l)))

##2. subtract 1 from all the elements inside the list
l=[1,2,3,4,590,80,90]
def s(u):
    return u-1
print(list(map(s ,l)))

##3. find the len of the strings present inside the list
a=["apple","mango","graps","kiwi","egg","f",]
print(list(map(len,a)))
print("----------------------------------------")
