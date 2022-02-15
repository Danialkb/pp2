from math import *
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f'Current coordinates: ({self.x};{self.y})')
    
    def move(self, xnew, ynew):
        self.x = xnew
        self.y = ynew
        print(f'Coordinates have been changed: ({self.x};{self.y})') 
    
    def dist(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
        print(sqrt( pow(self.x-d1, 2) + pow(self.y - d2, 2)))
P1 = Point(int(input()), int(input()))
P1.show()
P1.move(int(input()), int(input()))
P1.dist(int(input()), int(input()))