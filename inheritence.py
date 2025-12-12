# inheritence
class Animal:
    alive = True
    
    def eat(self):
        print("The animal is eating:")
        
    def sleep(self):
        print("The animal is sleeping: ")
class Rabbit(Animal):
    def sprint(self):
        print("The Rabbit is sprinting: ")
class Fish(Animal):
    def swim(self):
        print("The fish is swimming: ")
class Hawk(Animal):
    def fly(self):
        print("The Hawk is flying: ")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
rabbit.sprint()
fish.swim()
hawk.fly()
