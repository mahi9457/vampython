num1 = int(input("Enter the value of First number : "))
num2 = int(input("Enter the value of Second number : "))
num3 = int(input("Enter the value of Third number : "))

if(num1 > num2 and num1 > num3):
    print(num1,"is greater than others")
elif(num2 > num1 and num2 > num3):
    print(num2,"is greater than others")
elif(num3 > num2 and num3 > num1):
    print(num3,"is greater than others")