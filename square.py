from polygon import Polygon

class Square(Polygon):
    def __init__(self,height):
        super().__init__(height,height)
    def getArea(self):
        return self.height**2
    def getPerimeter(self):
        return self.height*4
squar = Square(5)
print("Kvadrat yuzasi = ", squar.getArea())
print("Kvadrat peremetri = " , squar.getPerimeter())