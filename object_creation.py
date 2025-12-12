class Vehicle:
    def __init__(self, name , speed):
        self.name = name
        self.speed = speed

    def increase_speed(self , increment):
        self.speed += increment
        print("New speed is: " , self.speed)
    
    
class Car(Vehicle):
    def __init__(self, name , speed, tire_type):
        super().__init__(name, speed)
        self.tire_type = tire_type
        
    def change_type(self, new_tire_type):
        self.tire_type = new_tire_type
        print("New tire type: " , self.tire_type)
        
    def color_type(self , color):
        self.color_type = color
        print("New colour is :" , self.color_type)
        
    def year(self, year):
        self.year = year 
        print("The year is: ", self.year)
        
    def price(self, price):
        self.price = price 
        print("The year is: ", self.price)
        
    def country(self , country):
        self.country = country
        print("The country Audi is from:" , self.country)

my_car = Car("Audi" , 120,"All-Season")
my_car.increase_speed(80)
my_car.change_type("Winter")
print("The car name is: " ,my_car.name)
my_car.color_type("White")
my_car.year("2026")
my_car.price("£145,000")
my_car.country("Italy")