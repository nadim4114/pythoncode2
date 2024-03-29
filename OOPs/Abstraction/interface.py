# When a class has all the methods as static methods then the class becomes an interface

from abc import ABC, abstractmethod
class BMW(ABC): # To make a class abstract class, we need to inherit from abstract class from ABC module
    def __init__(self, model, year):
        self.model = model
        self.year = year
    @staticmethod # When a class has all the methods as static then it becomes an interface
    def start(self):
        pass

    @staticmethod # When a class has all the methods as static then it becomes an interface
    def stop(self):
        pass
    @staticmethod # When a class has all the methods as static then it becomes an interface
    def drive(self):
        pass


class ThreeSeries(BMW):
    def __init__(self, cruiseControl, model, year):
        super().__init__(model, year)
        self.__cruiseControl = cruiseControl #assign value to private field

    def displayfeatures(self):
        print(f"Cruise control is {self.__cruiseControl}")

    def start(self):# over riding functionality from the parent class

        print("Button Starting")
    def stop(self):
        print("stopping with button")
    def drive(self):
        print("Three series is being driven")


class FiveSeries(BMW):
    def __init__(self,parkAssist, model, year):
        super().__init__(model, year)
        self.__parkAssist = parkAssist #assign value to private field

    def displayfeatures(self): #Private fields
        print(f"Parking assist is {self.__parkAssist}")

    def start(self): # over riding functionality from the parent class
        print("Remote Starting")

    def stop(self):
        print("Stopping via remote")
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
