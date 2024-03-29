class Duck:
    def Talk(self):
        print("Quack Quack")

class Human:
    def Talk(self):
        print("Hello")

class Dog:
    def Talk(self):
        print("Bow wow")


def callTalk(obj):
    obj.Talk()

d = Duck()
callTalk(d)


h = Human()
callTalk(h)


l = Dog()
callTalk(l)