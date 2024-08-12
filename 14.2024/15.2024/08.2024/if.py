speed = int(input("enter ur speed: "))
if(speed>0 and speed<40):
    print("safe for driving")
elif(speed>40 and speed<60):
    print("safe driving")
elif(speed>60 and speed<80):
    print("warning")
elif(speed>80):
    print("danger")
else:
    print("vehicle yet to start")
    







