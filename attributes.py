class Person:
    def __init__(self , name , surname):
        self._name = name   # protected attribute 
        self.__surname = surname  # private attribute
        
    def getter(self):
        return self._name

    def setter(self):
        return self.__surname

me = Person("Sasuke" , "Uchiha")

print(me.getter())
print(me.setter())
