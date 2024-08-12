###MULTIPLICATION TABLE(1 to 5)
##i = 1
##while i<=5 :
##    print(f"MULTIPLICATION TABLE FOR {i} :")
##    for j in range(1,11):
##        print(f"{i} x {j} = {i*j}")
##    print()
##    i+=1
##SECURITY
##CorrectUsername = input("ENTER USER :")
##CorrectPassword = input("ENTER PASSWORD :")
##attempts = 0
##MaxAttempts = 2
##
##while attempts < MaxAttempts:
##    Username = input("ENTER U R USERNAME :")
##    Password = input("ENTER U R PASSWORD :")
##    if(CorrectUsername == Username and CorrectPassword == Password):
##        print("LOGIN SUCCESSFULLY")
##        break
##    else:
##        print("INCORRECT USERNAME OR PASSWORD , PLS TRY AGAIN")
##        attempts += 1
##else :
##    print("MAX NO OF ATTEMPTS REACHED , ACCESS DENIED")



#1)multiplication tables upto 5th table using for loop:
for i in range(1,6):
    print(f"multiplication table of {i} : ")
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}")
    print("")



#2)multiplication tables upto 5th table using for while:
i = 1
while i <= 5 :
    print(f"multiplication table of {i} : ")
    j = 1
    while j <=10:
        print(f"{i} x {j} = {i*j}")
        j+=1
    i+=1
    print("_")
#3)  *
#    **
#    ***
#    ****
#    *****

for i in range(1,6):
    print("* "* i)
print("_")

#4)   1
#     1 2
#     1 2 3
#     1 2 3 4 
#     1 2 3 4 5


for i in range (1,6):
    for j in range(1,i+1):
        print(j," ",end = "")
    print()
print("_")
#5)  a
#    a b
#    a b c
#    a b c d
#    a b c d e 


for i in range(97 , 102):
    for j in range(97,i+1):
        print(chr(j)," ",end="")
    print()
print("_")
#6)  1  2  3   4   5
#    2  4  6   8   10
#    3  6  9   12  15
#    4  8  12  16  20
#    5  10 15  20  25


for i in range(1,6):
    for j in range(1,6):
        print(i*j," ",end="")
    print()
print("_")
