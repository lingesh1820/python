##multiplication table upto 5 using while loop

i=1
while i<=5:
    print(f"multiplication of table {i}: ")
    j=1
    while j<=10:
        print(f"{i}x{j}={i*j}")
        j+=1
    i+=1


for i in range (1,6):
    print("*"*i)



for i in range(1,6):
    for j in range(1,i+1):
        print(j,"",end="")
    print()


for i in range (97,102):
    for j in range(97,i+1):
        print(f"{chr(j)} ",end="")
    print()
