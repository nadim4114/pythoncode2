# Dependency injection or Polymorphism
# Car can have many engine type and based on engine type the car responds differently

class Car:
    def __init__(self, engine):
        self.engine = engine

    def typeEngine(self):
        self.engine.type()
    def start(self):
        self.engine.start()

    def speedLimit(self):
        self.engine.speedLimit()

class Hybrid:
    def type(self):
        print("This is hybrid engine")

    def start(self):
        print("This engine starts on fuel and runs on battery")

    def speedLimit(self):
        print("This is hybrid engine so Car's speed limit is 200 kmph")
class CNG:
    def type(self):
        print("This is CNG engine")

    def start(self):
        print("This engine starts on Petrol and runs on CNG")

    def speedLimit(self):
        print("This is CNG engine so Car's speed limit is 80 kmph")
class Petrol:
    def type(self):
        print("This is Petrol engine")

    def start(self):
        print("This engine starts on Petrol and runs on Petrol")

    def speedLimit(self):
        print("This is Petrol engine so Cas's speed limit is 150 kmph")

h = Hybrid()
c = CNG()
p = Petrol()

v = Car(h)
v.typeEngine()
v.start()
v.speedLimit()
