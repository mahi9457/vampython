number = int(input("Enter the number yu want to check : "))
filter = number%2

if(filter == 0):
    print(" Your entered number is EVEN")
elif(filter != 0):
    print(" Your entered number is ODD")