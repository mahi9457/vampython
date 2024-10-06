"""Create student class that takes name & marks of 3 subjects as arguments in consturtor. Then create method to print the average."""

class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def average(self):
        average = 0
        for value in self.mark:
            average += value
        print(f"Average : {average/3}")
s1 = student('Mahi',[50,50,50])
s1.average()
