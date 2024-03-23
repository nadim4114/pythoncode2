class Student:
    def set_id(self,id):
        self.__id = id
    def set_name(self,name):
        self.name = name

    def get_id(self):
        return(self.__id)


s = Student()
s.set_id(191)
s.set_name("Johan")

a = Student()
a.set_id(241)
a.set_name("Laalu")



print(s.name) # name is public field so its accessible directly
print(s.get_id()) # id is private field so we cannot access directly so method is required or name mangling

print(a.name) # name is public field so its accessible directly
print(a.get_id()) # id is private field so we cannot access directly so method is required or name mangling