#Class Point Represent a point in 2D space. Add methods to set coordinates and calculate distance from another Point object.
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(0, 0)

print("Distance:", p1.distance(p2))  
p1.set_coordinates(1, 1)
print("Updated Point:", p1)         
