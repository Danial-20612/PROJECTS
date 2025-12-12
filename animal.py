class Animal:
    def __init__(self, name: str):
        self.name = name

#This defines a method that should be implemented by subclasses.
#It “reserves” the speak() behavior but doesn’t define it.
#Raising NotImplementedError means: “If a subclass doesn’t override this, the program should fail.”
#This enforces that every specific animal must define how it speaks.

    def speak(self) -> str:
        raise NotImplementedError
 
#This is a special method (__str__), called when you use print() on an object.
#self.__class__.__name__ dynamically gets the class name (Dog, Cat, etc.).
#So print(Dog("Rex")) becomes <Dog name=Rex>.
 
    def __str__(self):
        return f"<{self.__class__.__name__} name={self.name}>"

#Inheritance
#Each subclass inherits from Animal and overrides speak() to behave differently.  
#A Dog is an Animal (it inherits everything from Animal).
#But it defines its own speak(): barking.
class Dog(Animal):
    def speak(self):
        return f"Woof! I'm {self.name}"

 
#Same pattern: each subclass defines its own version of speak().
#This is method overriding — a key OOP concept.
class Cat(Animal):
    def speak(self):
        return f"Meow. I'm {self.name}"
 
class Cow(Animal):

    def speak(self):
        return f"Moo... I'm {self.name}"
 
#This function expects a list of Animal objects.
#It loops through each a and calls its speak() method.
#Because of polymorphism, Python automatically calls the right version:
#If a is a Dog, it calls Dog.speak().
#If a is a Cat, it calls Cat.speak().(Method Overriding)

class Bird(Animal):

    def speak(self):
        return f"Chirp... I'm {self.name}"
 
def chorus(animals):
    return [a.speak() for a in animals]
 
#Creates a list called herd with one of each animal.
#Calls chorus(herd) → gets a list of all the speak() results.
#Prints each line — each animal’s “voice”.
#Then prints the string form of the first animal (a Dog).
 
def main():
    herd = [Dog("Rex"), Cat("Luna"), Cow("Betsy"), Bird("Pershia")]
    for line in chorus(herd):
        print(line)
    print(str(herd[0]))
 
if __name__ == "__main__":
    main()
 
    

 