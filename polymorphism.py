class Bird:
    def fly(self):
        print("Flying in the sky: ")

class Pengiun(Bird):
    def fly(self):
        print("Cannot fly, but swims really well: ")
        
eagle = Bird()
pengiun = Pengiun()
eagle.fly()
pengiun.fly()