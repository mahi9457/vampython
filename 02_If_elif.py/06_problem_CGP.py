name = input("Please Enter the student's Name : ")
marks = int(input(" Enter the student's Marks : "))

if(marks >= 90):
    print(name,"has'A' grade")
elif(marks < 90 and marks >= 80):
    print(name,"has'B' grade")
elif(marks < 80 and marks >= 70):
    print(name,"has'C' grade")
elif(marks < 70 and marks >= 60):
    print(name,"has'D' grade")
else:
    print("OOPS! You are fail ")