"""Hiding the inplementation details of a calss and only showing the essential features to the user """
#  hiding the unnecessary data or information

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluth = False
    def start(self):
        self.acc = True
        self.cluth = True
        print("Car is started...")
car = Car()
car.start()