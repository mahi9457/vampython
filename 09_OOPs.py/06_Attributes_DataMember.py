"""  Class & Instance Attributes  """
class BCA:
    college_name = "ITS (Mohan Nagar)"          #  Class Attributes
    def __init__(self,name,roll_no):
        self.name = name                        #  Instance Attributes
        self.roll_no = roll_no                  #  Instance Attributes
        print(BCA.college_name)
        print(self.name,self.roll_no)

student1 = BCA("Mahi",23103)
student2 = BCA("Tanya",23190)