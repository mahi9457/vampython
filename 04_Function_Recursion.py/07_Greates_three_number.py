def greatest_three():
    n1 = int(input("Enter the First number : "))
    n2 = int(input("Enter the Second number : "))
    n3 = int(input("Enter the Third number : "))
    if(n1>n2 and n1>n3):
        print(f"{n1} is greater than other")
    elif(n2>n1 and n2>n3):
        print(f"{n2} is greater than other")
    elif(n3>n2 and n3>n1):
        print(f"{n3} is greater than other")


greatest_three()