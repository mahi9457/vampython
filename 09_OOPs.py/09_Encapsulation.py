""" Wrapping data and functions into a single unit(object)"""

class family:
        @staticmethod
        def getdata():
            name = input("Enter your name : ")
            income = int(input("Enter your income : "))
        def putdata(self):

            print("Name is ",name)
            print(f"{name}'s income is : ",income)
            
p1 = family()
p1.getdata()
p1.putdata()
