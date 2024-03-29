# Abstraction is the process of defining overview and mandating certain features that all
# the classes should follow that inherit from Abstract class
from abc import ABC, abstractmethod
class BMW(ABC): # To make a class abstract class, we need to inherit from abstract class from ABC module
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start(self):
        print("Method to start the car")

    def stop(self):
        print("Stopping the car")
    @abstractmethod # At least 1 abstract method should be there for a class to be abstract
    def drive(self):
        pass


class ThreeSeries(BMW):
    def __init__(self, cruiseControl, model, year):
        super().__init__(model, year)
        self.__cruiseControl = cruiseControl #assign value to private field

    def displayfeatures(self):
        print(f"Cruise control is {self.__cruiseControl}")

    def start(self):# over riding functionality from the parent class
        super().start()
        print("Button Starting")

    def drive(self):
        print("Three series is being driven")


class FiveSeries(BMW):
    def __init__(self,parkAssist, model, year):
        super().__init__(model, year)
        self.__parkAssist = parkAssist #assign value to private field

    def displayfeatures(self): #Private fields
        print(f"Parking assist is {self.__parkAssist}")

    def start(self): # over riding functionality from the parent class
        super().start()
        print("Remote Starting")

    def drive(self):
        print("Five series is being driven")

t = ThreeSeries("Enabled","2", 2022)
t.displayfeatures()
t.start()
t.drive()
t.stop()


f = FiveSeries("Enabled","3", 2024)
f.displayfeatures()
f.start()
f.drive()
f.stop()
