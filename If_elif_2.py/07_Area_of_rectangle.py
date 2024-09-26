# Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter. ??

l = int(input("Enter the length of the Rectangle :"))
b = int(input("Enter the breadth of the Rectangle :"))

area = l*b
print("Area :",area)

perimeter = 2*(l+b)
print("Perimeter :",perimeter)
 
if(area > perimeter):
    print("Area is greater than Perimeter")
elif(area < perimeter):
    print("Perimeter is greater than Area")