 
from random import *

##Tasks:
##
##1. create a list and use random module and apply the below functions:
##choice, choices, random, randrange, randint,sample
##2. use while loop and random module to build a rock paper scissor game and print who won the game!
5


##1. create a list and use random module and apply the below functions:
##choice, choices, random, randrange, randint,sample
##l=[1,12,3,4,45,66,7,129]
##
####choice
##
##print(choice(l))
##print("-----------------------------------------------------------------")
####choices
##
##print(choices(l,k=129))
##print("-----------------------------------------------------------------")
##
####random
##
##print(random())
##print("-----------------------------------------------------------------")
##
####randrange
##
##print(randrange(1,10))
##print("-----------------------------------------------------------------")
##
####randit
##
##print(randint(1,10))
##print("-----------------------------------------------------------------")
##
####sample
##
##print(sample(l,k=2))
##print("-----------------------------------------------------------------")



##2. use while loop and random module to build a rock paper scissor game and print who won the game!
##import random
##print("welcome to the game sir/madam")
##user_input=0
##computer_input=0
##max_chance=0
##option=["stone","paper","scissor"]
##computer=random.choice(option)
##print(computer)
##while max_chance<3:
##    user=input("enter a option(/stone/paper/scissor): ")
##    computer=random.choice(option)
##    if user == computer:
##        print("its a tie, pls try again" )
##    elif (user == "paper" and computer == "rock") or (user == "scissor" and computer == "paper") or (user == "rock" and computer == "scissor"):
##        print("user wons the game")
##        user_input+=1
##    else:
##        print("computer wons the game")
##        computer_input+=1
##    print("user score",user_input)
##    print("computer score",computer_input)
##    if user_input>=5 or computer_input>=5:
##        break
##if user_input>computer_input:
##    print("user wons the game")
##else:
##    print("computer wons the game")
##
##print("thanks for playing")

print("-----------------------------------------------------------------------")
import random
print("welcome to the game sis/madam")
i=0
chocolate= ["kitkat","diarymilk","milkybar","5star","snickers","kinderjoy","gems"]
computer= random.choice(chocolate)
print(computer)
attempts = 0
while i < 3:
    user=input ("enter ur option\n(kitkat/diarymilk/milkybar/5star/snickers/kinderjoy/gems):")
    if user == computer :
        print("u won the game , by choosing the crt chocolate")
        play_again = input("enter yes u want to play again or no :")
        if  play_again == "yes" :
            print("welcome to the game sir or madam")
            attempts+=1
        else :
            print("thanks for playing")
            break

    else:
        print(f"u lost the game , by choosing the wrong chocolate,try again")
        attempts+=1

    




        







    





























        
            

        

    
    
