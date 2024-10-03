import random

computer = random.randint(1,100)
print("Choose the between (1,100)")

while True:
        you = int(input("Enter the number  : "))
        if(computer == you):
            print("You Guss the CORRECT Number! ")
            print("---------Game Over---------")
            break
        elif(computer < you):
            print(" Please Guess the smaller one")
        else:
            print(" Please Guess larger Number")  
