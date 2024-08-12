##control statments
##break statment
##continue statment
##pass statment


##break statment

##for i in range(9):
##    if i==7:
##        break
##    else:
##        print(i)





##i=1
##while i<=9:
##    if i ==7:
##        break
##        print (i)
##        i+=1
##    else:
##        print(i)
##        i+=1
##

##l = [-5, 2, 0, 7, -3, 0, 4]
##
##Hint: Assign separate variable to store results.
##
##1. Count the number of positive, negative, and zero values in a list
##2. Sum all the positive numbers from the above list.
##
##3. Print all even numbers under 20 using while loop (3 different cods using normal while, using continue, using pass)
##4. count the total number of vowels from a string.
##
##5. check whether the given number is a prime number
##	Prime number means: a number being divided only by 1 and itself. eg: 1,3,5,7
##
##6. find the maximum value from the list using loop
##7. Print Fibonacci series up to 50.
##	fibonacci series eg: 0,1,1,2,3,5,8,13,21,34
##

##1. Count the number of positive, negative, and zero values in a list

d = [-5, 2, 0, 7, -3, 0, 4]
pos=0
neg=0
zero=0
for i in d:
    if i> 0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zero+=1
print("positive numbers",pos)
print("negative numbers",neg)
print("zero numbers",zero)
    
    

##2. Sum all the positive numbers from the above list.

d = [-5, 2, 0, 7, -3, 0, 4]
sum=0
for i in d:
    if i>0:
        sum+=i
print(sum)
##    
##
####3. Print all even numbers under 20 using while loop (3 different cods using normal while, using continue, using pass)
##
##i=0
##while i <20:
##    i+=2
##    print("even number",i)
##
##i=1
##while i < 20:
##    if i%2 != 0:
##        i+=1
##        print(i,"even number")
##        continue
##    else:
##        i+=1
##8        
##i=0
##while i<20:
##    if i%2 !=0:
##        i+=1
##        print("even number",i)
##        pass
##    else:
##        i+=1
##
    
##4
        
a=input("enter a word: ")
count=0
for i in a:
    if i in("aeiou"):
        count+=1
print("the total number of vowel words are",a,"is",count)























