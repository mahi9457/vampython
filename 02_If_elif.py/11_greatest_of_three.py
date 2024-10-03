# Take 3 positive integers input and print the greatest of them. 

n1 = int(input("Enter the first Number : "))
n2 = int(input("Enter the Second Number : "))
n3 = int(input("Enter the third Number : "))

if(n1 > n2 and n1 > n3):
    print(n1,"is greater then other ")
elif(n2 > n1 and n2 > n3):
    print(n2,"is greater then other ")
elif(n3 > n2 and n3 > n1):
    print(n3,"is greater then other ")