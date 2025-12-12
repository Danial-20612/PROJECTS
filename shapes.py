class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle 🟢"

class Square(Shape):
    def draw(self):
        return "Drawing a Square 🟦"

class Triangle(Shape):
    def draw(self):
        return "Drawing a Triangle 🔺"

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "triangle":
            return Triangle()

factory = ShapeFactory()
triangle = Triangle()
circle = Circle()
square = Square()
response = input("Enter the shape name: triangle , circle, square: ")
if response == "triangle":
    print(triangle.draw())
    
elif response == "circle":
    print(circle.draw())
    
elif response == "square":
    print(square.draw())
    