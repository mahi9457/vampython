class student:
    @staticmethod
    def hello():               # static methods
        print("Hello!")
    def show_info(self,name,marks):      # self methods
        self.name = name
        self.marks = marks
        print(self.name,self.marks)

s1 = student()
s1.show_info("Mahi",69)
