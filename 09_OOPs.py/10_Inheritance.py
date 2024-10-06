class car:
    def start(self):
        print("Car started...")
    def stop(self):
        print("Car stoped...")
class nano(car):
    clour = "red"
c1 = nano()
c1.start()
c1.stop()
print("Car colour is ",c1.clour)