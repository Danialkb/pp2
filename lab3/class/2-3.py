class Shape:
    def __init__ (self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__ (self, len):
        self.len = len
    
    def area(self):
        return self.len**2

class Rectangle(Shape):
    def __init__ (self, len, wid):
        self.len = len
        self.wid = wid
    
    def area(self):
        return self.len*self.wid
        
S1 = Square(int(input()))
Sh1 = Shape()
R1 = Rectangle(int(input()), int(input()))
print(Sh1.area())
print(S1.area())
print(R1.area())