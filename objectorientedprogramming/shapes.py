class Shapes:
    def __init__(self,name):
        self.name = name

class Parallelogram(Shapes):
    base : int
    height : int
    def __init__(self,name,base,height):
        super().__init__(name)
        self.base = base
        self.height = height
    def area(self):
        print("area of",self.name,"=",self.base * self.height)

p_instance = Parallelogram("parallelogram",12,15)
p_instance.area()

class Rectangle(Shapes):
    length : int
    width : int
    def __init__(self,name,length,width):
        super().__init__(name)
        self.length = length
        self.width = width
    def area(self):
        print("area of",self.name,"=",self.length * self.width)

r_instance = Rectangle("Rectangle",12,14)
r_instance.area()

class Circle(Shapes):
    radius:float
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = radius
    def area(self):
        print("area of",self.name,"=",3.14*self.radius**2)

c_instance = Circle("Circle",9)
c_instance.area()

class Square(Shapes):
    length : int
    def __init__(self,name,length):
        super().__init__(name)
        self.length = length
    def area(self):
        print("area of",self.name,"=",self.length **2)

s_instance = Square("square",12)
s_instance.area()

class Trapezium(Shapes):
    side1: int
    side2 : int
    height : int
    def __init__(self,name,side1,side2,height):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.height = height
    def area(self):
        print("area of",self.name,"=",((self.side1+self.side2)+self.height)/2)

t_instance = Trapezium("Trapezium",5,6,12)
t_instance.area()


    




    
