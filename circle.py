from math import pi
class Circle:
    def __init__(self, r) -> None:
        self.r = r

    def getArea(self):
        """
        This method finds the area of the Circle.

        Args:
            No
        Returns:
            float or int: result.
        """
        return self.r*self.r*pi if self.r>0 else False

    def getLength(self):
        """
        This method finds the length of the cirle.

        Args:
            No
        Returns:
            float or int: result..
        """
        return 2*self.r*pi if self.getArea()!=False else False
radius = Circle(4.5)
print(radius.getArea())
print(radius.getLength())