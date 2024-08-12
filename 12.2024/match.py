print("WELCOME TO OUR PIZZA SHOPE")
option=int(input("enter 0 or 1 \n 0= samll pizza \n 1= large pizza ,\n which one do u want:  " ))
smallpizza = 40
largepizza = 90
toppinnsprice   = 10
match option:
    case 0:
        print(" u have selected small pizza ")
        q= int(input("how many pizza do u want : "))
        TotalAmount = smallpizza*q
        print(" ur total amount is ",TotalAmount)
        print("if u need toppinns select 2 other wise press 3 ")
        toppinns = int(input("select the option: "))
        match toppinns:
            case 2:
                print("u have choosed toppinns")
                Q=int(input("many pack do u want: "))
                totalamount=(toppinnsprice*Q)+TotalAmount
                print("ur totalamount is",totalamount)
                cost=int(input("pls psy the above amount: "))
                if(cost>=totalamount):
                    if(cost==totalamount):
                        print("thank u")
                    else:
                        print(cost-totalamount,"here is ur change")
            case 3:
                print("u does not need toppinns")
                print("thanks for visiting our shop")
    case 1:
        print("u have selected large pizza")
        q=int(input("how many pizza do u want: "))
        TotalAmount=largepizza*q
        print("ur total amount is ",TotalAmount)
        print("if u need toppinns select 2 other wise select 3")
        toppinns=int(input("select the option:"))
        match toppinns:
            case 2:
                print("u have choosed toppinns")
                toppinnsquantity=int(input("how many pack do u want: "))
                totalamount=(toppinnsprice*toppinnsquantity)+TotalAmount
                print("ur total amount is",totalamount)
                cost=int(input("pls pay the above amount:"))
                if(cost>=totalamount):
                    if(cost==totalamount):
                        print("thank u")
                    else:
                        print(cost-totalamount,"here is ur change:")
            case 3:
                print("u do not need toppinns")
                print("thanks for visiting our shope")
                
    
                
                
