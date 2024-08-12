## user defined functions

##Tasks using def:-
##1. define a function to find whether a number is even or odd
##2. define a function to find whether a string is palindrome or not (return True or False)
##3. define a function with (* args) arbitrary arguments condition(*)
##4. define a function with (* * kwargs) arbitrary keyword arguments()
##5. define a function to find the sum of the list
##6. define a function to find the second largest number
##7. define a function to find whether a number is prime or not



##l=[]
##def even (*numbers):
##    for i in numbers:
##        if i %2 ==0 :
##            l.append (i)
##    return l
##    
##
##even(1,2,3,4,5,6,7,8,9)
##print(l)

##1. define a function to find whether a number is even or odd

##def even_number_is (number):
##    if number % 2==0:
##        return "even"
##    else:
##        return "odd"
##a=int(input("enter a number:"))
##print(even_number_is (a))
##
##
####2. define a function to find whether a string is palindrome or not (return True or False)
##def ispalindrome (i):
##    if (i==i[::-1]):
##        return "true"
##    else:
##        return "false"
##a=input("enter a word:")
##print(ispalindrome (a))
##    
####3. define a function with (* args) arbitrary arguments condition(*)
##def m (*numbers):
##    total =1
##    for i in numbers:
##        total*=i
##    return total
##print(m(30,48))
##print()
##
##
####4. define a function with (* * kwargs) arbitrary keyword arguments()
##def name (**name):
##    print("the firstname is ",name["firstname"])
##name(firstname = "lingesh" ,lastname = "sakthivel")
##print()
##
##
####5. define a function to find the sum of the list
##def sum_l (number):
##    total=0
##    for i in number:
##        total+=i
##    return total
##print(sum_l([3,4,5,6,7,8,9]))
##print()

##6. define a function to find the second largest number
##def second_largest (number):
##    number.sort()
##    return("secound largest no is",number[-2])
##print(second_largest([100,999,24546,8,9,245]))##1. Factorial Calculation
##Problem: Compute the factorial of a number n (denoted as n!).
##
##Recursive Solution:
##
##python
##Copy code
##def factorial(n):
##    if n == 0:
##        return 1
##    else:
##        return n * factorial(n - 1)
##
##print(factorial(5))  # Output: 120
##2. Fibonacci Sequence
##Problem: Find the n-th number in the Fibonacci sequence.
##
##Recursive Solution:
##
##python
##Copy code
##def fibonacci(n):
##    if n <= 1:
##        return n
##    else:
##        return fibonacci(n - 1) + fibonacci(n - 2)
##
##print(fibonacci(5))  # Output: 5
##3. Power of a Number
##Problem: Compute x raised to the power of n (x^n).
##
##Recursive Solution:
##
##python
##Copy code
##def power(x, n):
##    if n == 0:
##        return 1
##    else:
##        return x * power(x, n - 1)
##
##print(power(2, 3))  # Output: 8
##4. Sum of Elements in a List
##Problem: Calculate the sum of all elements in a list.
##
##Recursive Solution:
##
##python
##Copy code
##def sum_list(lst):
##    if not lst:
##        return 0
##    else:
##        return lst[0] + sum_list(lst[1:])
##
##print(sum_list([1, 2, 3, 4, 5]))  # Output: 15
##5. Reverse a String
##Problem: Reverse a string.
##
##Recursive Solution:
##
##python
##Copy code
##def reverse_string(s):
##    if len(s) == 0:
##        return s
##    else:
##        return reverse_string(s[1:]) + s[0]
##
##print(reverse_string("hello"))  # Output: "olleh"
##
##print()
##











##1

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

print(power(2, 1))

##2

def sumlist (numbers):
    if not numbers:
        return  0
    else:
        return numbers[0]+sumlist(numbers[1:])
print(sumlist([1,3,4,5,67,8]))
print()
82
##3

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))  # Output: 5

