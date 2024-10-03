import random

computer = random.choice(["snake","gun","water"])
you = input("Enter your choice (snake/gun/water) :  ")
print("Computer chose : ",computer)

if(computer == you):
    print("It's draw")
else:
    if(computer == "snake" and you == "gun"):
        print("You WIN :)")
    elif(computer == "snake" and you == "water"):
        print("You LOSE :(")
    elif(computer == "water" and you == "snake"):
        print("You WIN :)")
    elif(computer == "water" and you == "Gun"):
        print("You LOSE :(")
    elif(computer == "gun" and you == "snake"):
        print("You LOSE :()")
    elif(computer == "gun" and you == "water"):
        print("You WIN :)")
    elif(computer == "water" and you == "gun"):
        print("You LOSE :(")
    else:
        print("Something wrong")