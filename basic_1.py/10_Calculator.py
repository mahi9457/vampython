n = int(input("Enter the first Number : "))
operator = input("Enter the operation (+,-,*,/) : ")
n2 = int(input("Enter the Second Number : "))
 
if(operator == "+"):
    print(n+n2)
elif(operator == "-"):
    print(n-n2)
elif(operator == "*"):
    print(n*n2)
elif(operator == "/"):
    print(n/n2)
else:
    print(operator,"is not vailed for the calculation ")