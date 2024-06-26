# https://www.youtube.com/watch?v=XI7zep97c-Y



# Single Responsibility Principle (SRP)
class FileHandler: 
    def read_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()
    
    def write_file(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)

# Open/Closed Principle (OCP)
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Liskov Substitution Principle (LSP)
def calculate_area(shape):
    return shape.area()

# Interface Segregation Principle (ISP)
class Worker:
    def work(self):
        pass

class Eater:
    def eat(self):
        pass

class Human(Worker, Eater):
    def work(self):
        print("Working...")
    
    def eat(self):
        print("Eating...")

# Dependency Inversion Principle (DIP)
class LightBulb:
    def __init__(self):
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

class Switch:
    def __init__(self, bulb):
        self.bulb = bulb
    
    def operate(self):
        if self.bulb.is_on:
            self.bulb.turn_off()
        else:
            self.bulb.turn_on()

# Example usage
if __name__ == "__main__":
    # SRP
    file_handler = FileHandler()
    file_handler.write_file("example.txt", "Hello, SOLID principles!")
    content = file_handler.read_file("example.txt")
    print("File content:", content)
    
    # OCP
    circle = Circle(5)
    print("Circle area:", circle.area())
    
    # LSP
    circle = Circle(7)
    print("Area calculated using LSP:", calculate_area(circle))
    
    # ISP
    human = Human()
    human.work()
    human.eat()
    
    # DIP
    bulb = LightBulb()
    switch = Switch(bulb)
    switch.operate()
    print("Bulb is on:", bulb.is_on)
