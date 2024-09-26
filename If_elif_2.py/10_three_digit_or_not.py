# Take positive integer input and tell if it is a three digit number or not.

n = int(input("Enter the Number : "))

if(n > 99 and n < 1000):
    print("Number has three digit")
else:
    print("Number has not three digit")
