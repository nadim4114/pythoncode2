class BMW:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start(self):
        print("Method to start the car")

    def stop(self):
        print("Stopping the car")

class ThreeSeries(BMW):
    def __init__(self, cruiseControl, model, year):
        super().__init__(model, year)
        self.__cruiseControl = cruiseControl #assign value to private field

    def displayfeatures(self):
        print(f"Cruise control is {self.__cruiseControl}")

    def start(self):# over riding functionality from the parent class
        super().start()
        print("Button Starting")


class FiveSeries(BMW):
    def __init__(self,parkAssist, model, year):
        super().__init__(model, year)
        self.__parkAssist = parkAssist #assign value to private field
        print(super())
    def displayfeatures(self): #Private fields
        print(f"Parking assist is {self.__parkAssist}")

    def start(self): # over riding functionality from the parent class
        super().start()
        print("Remote Starting")


t = ThreeSeries("Enabled","2", 2022)
t.displayfeatures()
t.start()
t.stop()


f = FiveSeries("Enabled","3", 2024)
f.displayfeatures()
f.start()
f.stop()