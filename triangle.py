from polygon import Polygon
from math import sqrt

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getArea(self):
        if self.a > 0 and self.b > 0 and self.c > 0:
            half_perimeter = (self.a + self.b + self.c)/2
            return sqrt(half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))
        return 0
    def getPerimeter(self):
        if self.a > 0 and self.b > 0 and self.c > 0:
            return self.a + self.b + self.c
        return 0 

x = Triangle(3, 4, 5)
print(x.getPerimeter())