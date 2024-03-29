from abc import ABC, abstractmethod
class Vehicle(ABC):# Abstract class
    def __init__(self):
        pass

    def engine(self):
        pass


    def chassis(self):
        pass


    def paint(self):
        pass

    def vehicletype(self,range):
        self.range = range

class Car():
    def __init__(self,cmd, engine, chassis, noOfSeats):
        self.cmd = cmd
        self.__engine = engine
        self.__chassis = chassis
        self.noOfSeats = noOfSeats


    def start(self):
        print("Vehicle start")

    def engine(self):
        print("Engine type")

    def chassis(self):
        print("Chassis type")

    def noOfSeats(self):
        print("No of seats")

    def info(self):
        print(self.cmd, self.__engine, self.__chassis, self.noOfSeats)

class Engine:

    def CNG(self):
        print("This is CNG engine, this will run 80 kmph")

    def Petrol(self):
        print("This is Petrol engine, this will run 150 kmph")

    def EV(self):
        print("This is EV engine, this will run 200 kmph")

class SeatingCap:

    def sevenseater(self):
        print("This is seven seater car")
    def fiveseater(self):
        print("This is five seater car")

s = SeatingCap().fiveseater()
s1 = SeatingCap().sevenseater()
e = Engine()
e1 = Engine()

c = Car("start", e.EV(), "Steel", s)
c.info()
b = Car("start", e1.CNG(), "Steel", s1)




