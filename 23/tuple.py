##tuple
##1. create a tuple and add a new item to it
##2. create a tuple and remove an existing item
##3. unpack a tuple and assign to 2 variables i.e, a & b
##4. count the occurences of an item in a tuple
##5. concatenate two tuples
##6. remove all duplicates from the tuple using loop
##7. insert a list into the tuple and append an item to the list inside the tuple!
##8. create a set and add and remove an item in the set
##9. create a nested tuple and print the items of the nested tuple



##1. create a tuple and add a new item to it
tup = ("apple","banana","orange" ,"cherry","mango")
tup=list(tup)
tup.append("kiwi")
tup=tuple(tup)
print(tup)
print("--------------------------------------------------------")

##2. create a tuple and remove an existing item
tup = ("apple","banana","orange" ,"cherry","mango")
tup=list(tup)
tup.remove("orange")
tup=tuple(tup)
print(tup)
print("--------------------------------------------------------")

##3. unpack a tuple and assign to 2 variables i.e, a & b
tup = ("apple","banana","orange")
(a,*b)=tup
print("tup=",tup)
print("a=",a)
print("b=",b)
print("--------------------------------------------------------")

##4. count the occurences of an item in a tuple
tup = ("apple","banana","orange" ,"cherry","mango")*2
a=tup.count("apple")
b=tup.count("banana")
c=tup.count("orange")
d=tup.count("cherry")
e=tup.count("mango")
print("no of apple in tuple",a)
print("no of banana in tuple",b)
print("no of orange in tuple",c)
print("no of cherry in tuple",d)
print("no of mango in tuple",e)
print("--------------------------------------------------------")

##5. concatenate two tuples
a=(1,2,3,4)
b=(5,6,7,8)
c=()
c=a+b
print(c)
print("--------------------------------------------------------")

##6. remove all duplicates from the tuple using loop
tup = ("apple","banana","orange" ,"cherry","mango")*2
for i in tup:
    tup=set(tup)
    tup=tuple(tup)
print(tup)
print("--------------------------------------------------------")

##8. create a set and add and remove an item in the set
s={"apple","banana","orange" ,"cherry","mango"}
s.add("kiwi")
print(s)
s.remove("orange")
print(s)
print("--------------------------------------------------------")

##9. create a nested tuple and print the items of the nested tuple
tup=("apple",("banana","orange") ,("cherry"),"mango")
for i in tup:
    print(i)
print("--------------------------------------------------------")

##7. insert a list into the tuple and append an item to the list inside the tuple!
tup = (["apple","banana","orange" ,"cherry","mango"],)
a=tup[0]
a.append("kiwi")
print("--------------------------------------------------------")

print(tup)
