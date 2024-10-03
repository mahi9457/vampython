# Any year is input through the keyboard. Write a program to determine whether the year is a leap year or not.??

year = int(input("Enter the Year : "))

if(year % 4 == 0):
    print(year,"is a LEAP YEAR")
else:
    print(year,"is NOT LEAP YEAR")