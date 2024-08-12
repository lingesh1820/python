print("twelcome to lingeshwar grocery shop")
option=int(input("enter0 or 1 or 2 or 3 \n 0=rice per kg 100 \n 1=onion per kg 50 \n 2=tomato per kg 60 \n 3 potato per kg 70 \n kindly enter ur option: "))
if(option == 0):
    riceprice=100
    print("u have choosed rice")
    q=int(input("how many kg do u want: "))
    totalamt=riceprice*q
    print("the amt of rice is",totalamt)
    cost=int(input("pls pay the above amount: "))
    print("thanks for purchasing")
elif(option==1):
    onionprice=50
    print("u have choosed onion")
    q=int(input("how many kg do u want :"))
    totalamt=onionprice*q
    print("the amt of 0nion is",totalamt)
    cost= int(input("pls pay the above amount:"))
    print("thanks for purchasing")
elif(option==2):
     tomatoprice=60
     print("u have choosed tomato")
     q=int(input("how many kg do u want: "))
     totalamt=tomatoprice*q
     print("the amt of tomato is",totalamt)
     cost=int(input("pls pay the above amount: "))
     print("thanks for purchasing")
elif(option==3):
    potatoprice=70
    print("u have choosed potato")
    q=int(input("how many kg do u want:"))
    totalamt=potatoprice*q
    print("the amt of potato is",totalamt)
    cost=int(input("pls pay the above amount:"))
    print("thanks for purchasing")
else:
    print("u have choosed the wrong option")

    
    

        



    
 
