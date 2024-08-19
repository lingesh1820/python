##types of error
##1. ZeroDivisionError
##2. KeyError
##3. NameError
##4. ValueError
##5. IndexError
##6. TypeError

##try:
##    print("hello world")
##except:
##    print("error is found")
##else:
##    print("error is not found")
##finally:
##    print("nothing")

##1. ZeroDivisionError
try:
    print(5/0)
except:
    print("number cannot be divide by zero")
##2. KeyError
x={"a":-1,"b":2}
try:
    print(x["c"]) 
except :
    print("error is found")
    
##3. NameError
try:
    print(a)
except:
    print("variable a is not found")    
##4. ValueError
try:
    print(int["abc"])
except:
    print("str cannot be converted into int")
##5. IndexError
try:
    x=[1,2,3,4]
    print (x[5])
except :
    print("error is  found")
##6. TypeError
try:
    print("b"+1)
except :
    print("srt cannot be concadinate with int")


##nested try--except

try :
    a=int(input("enter a number:"))
    try:
        print(a/0)
    except:
        print("number cannot be divide by zero")
except:
    print("error is found")

    

