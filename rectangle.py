from polygon import Polygon

class Rectangle(Polygon):
    def getArea(self):
        return self.height*self.width
    def getPerimeter(self):
        return 2*(self.width + self.height)
rectang = Rectangle(3,4)
print(rectang.getArea())
print(rectang.getPerimeter())