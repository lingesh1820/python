##Tasks:
##1. create a dictionary and add 2 new items to it.
##2. Remove two key:value pairs from the dictionary
##3. check whether a key exists in the dictionay
##4. check whether a value exists in the dictionary
##5. update the key and value using if-else
##6. merge two dictionaries and store it in a variable 
##7. create a dictionary and print its values using loop
##8. create a nested dictionary and print its values using nested loop
##9. add new key,value pair to the nested dictionary


##1. create a dictionary and add 2 new items to it.
a={
    "name":"lingeshwar",
    "choosed course":"python"
    }
a.update({"course timing":"11 to 12.30"})
a.update({"place":"pondicherry"})
print(a)

print("------------------------------------------------------------------")


##2. Remove two key:value pairs from the dictionary


a={
    "name":"lingeshwar",
    "choosed course":"python",
    "course timing":"11 to 12.30",
    "place":"pondicherry"
    }
a.pop("course timing")
a.pop("place")
print(a)
print("------------------------------------------------------------------")
##3. check whether a key exists in the dictionay
a={
    "name":"lingeshwar",
    "choosed course":"python",
    "course timing":"11 to 12.30",
    "place":"pondicherry"
    }
key=input("enter a key:")
if key in a:
    print(" the key is present")
else:
        print(" the key is not present")
print("------------------------------------------------------------------")

##4. check whether a value exists in the dictionary
a={
    "name":"lingeshwar",
    "choosed course":"python",
    "course timing":"11 to 12.30",
    "place":"pondicherry"
    }
value=input("enter a value:")
if value in a.values():
    print(" the value is present")
else:
        print(" the value is not present")
print("------------------------------------------------------------------")

    
##5. update the key and value using if-else
a={
    "name":"lingeshwar",
    "choosed course":"python",
    "course timing":"11 to 12.30",
    "place":"pondicherry"
    }
key="course timing"
if key in a:
    a.update({"course timing":"1 to 4"})
    print(a)
else:
    a.update({"course timing":"1 to 4"})
    print(a)
print("------------------------------------------------------------------")

##6. merge two dictionaries and store it in a variable 
a={
    "name":"lingeshwar",
    "choosed course":"python"
    }
b={
    "course timing":"11 to 12.30",
    "place":"pondicherry"
    }
c={}
c.update(a)
c.update(b)
print(c)
print("------------------------------------------------------------------")

##7. create a dictionary and print its values using loop
a={
    "name":"lingeshwar",
    "choosed course":"python",
    "course timing":"11 to 12.30",
    "place":"pondicherry"
    }
for i in a.values():
    print(i)
print("------------------------------------------------------------------")

##8. create a nested dictionary and print its values using nested loop
a={
    "nashat":{"age":17,"city":"pondicherry","schooling":"amalorpavam hr sec school"},
    "sriram":{"age":18,"city":"cuddalor","schooling":"amalorpavam hr sec school"},
    "logeshwar":{"age":16,"city":"aurovil","schooling":"amalorpavam hr sec school"},}
for key , value in a.items() :
    print(f"details for {key}")
    for key,value in value.items():
        print( f"{key}:{value}")
        print()
    

        

    
