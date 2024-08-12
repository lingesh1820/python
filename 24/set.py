##set
##union


##method type
##a={1,2,3,4,5,6,7,8}
##b = {"a","b","c","d"}
##c=a.union(b)
##print(c)
##print("-------------------------------------------------------------------")
####operator type
##a={1,2,3,4,5,6,7,8}
##b = {"a","b","c","d"}
##c=a|(b)
##print(c)
##print("-------------------------------------------------------------------")
##
####intersection
####method type
a={1,2,3,4,5,6,7,8}
b = {"a","b","c","d",1,4,5,8}
c=a.intersection(b)
print(c)
print("-------------------------------------------------------------------")
##
####operator type
##
##a={1,2,3,4,5,6,7,8}
##b = {"a","b","c","d",1,4,5,8}
##c=a&(b)
##print(c)
##print("-------------------------------------------------------------------")
##
####difference
####method type
##a={1,2,3,4,5,6,7,8}
##b = {"a","b","c","d",1,4,5,8}
##c=a.difference(b)
##print(c)
##print("-------------------------------------------------------------------")
####operator type
##a={1,2,3,4,5,6,7,8}
##b = {"a","b","c","d",1,4,5,8}
##c=a-(b)
##print(c)
##print("-------------------------------------------------------------------")
##
####symmetric_difference
####method type
##a={1,2,3,4,5,6,7,8}
##b = {"a","b","c","d",1,4,5,8}
##c=a.symmetric_difference(b)
##print(c)
##print("-------------------------------------------------------------------")
####operator type
##a={1,2,3,4,5,6,7,8}
##b = {"a","b","c","d",1,4,5,8}
##c=a^(b)
##print(c)
##print("-------------------------------------------------------------------")
##





##SET Tasks:
##1. create a set - add 2 items and remove 2 items 
##2. print the union, intersection, difference, symmetric difference of two sets using operators
##3. check whether an item is present in the set or not using if else
##4. loop and print the elements of the set
##5. print the square of the items in the set.
##6. check whether the set is superset or subset
##7. convert a string to set


##1. create a set - add 2 items and remove 2 items 
a={1,2,3,4,5,6,7,8}
a.update({11,12})
print("no added:",a)
a.remove(11)
a.remove(12)
print(a)
print("---------------------------------------------------------------------------------")
##2. print the union, intersection, difference, symmetric difference of two sets using operators
a={1,2,3,4,5,6,7,8}
b={"a","b","c","d","e","f",4,5,8,1,3}
print("by using union",a|b)
print("by using intersection",a&b)
print("by using difference ",a-b)
print("by using symmetric",a^b)
print("---------------------------------------------------------------------------------")

##3. check whether an item is present in the set or not using if else
a=("mango","banana","kiwi","orange","apple")
checking=input("enter a fruit name: ")
if checking in a:
    print("present")
else:
    print("not present")
print("---------------------------------------------------------------------------------")

##4. loop and print the elements of the set
a={"a","b","c","d","e","f",4,5,8,1,3}
for i in a:
    print(i)
print("---------------------------------------------------------------------------------")

##5. print the square of the items in the set.
a={1,2,3,4,5,6,7,8}
for i in a:
    print("square of",i,i**2)
print("---------------------------------------------------------------------------------")

##6. check whether the set is superset or subset
a=(1,2,3,4,5,6,7,8)
b=(4,5,6,7)
if a.issuperset (b):
    print("true")
else:
    print("false")
if b .issubset (a):
    print("true")
else:
    ("false")
print("---------------------------------------------------------------------------------")

##7. convert a string to set
a="mango"
a=set(a)
print(a)
print("---------------------------------------------------------------------------------")
