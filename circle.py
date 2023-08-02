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
        r=self.r
        s=pi*r*r
        return s

    def getLength(self):
        """
        This method finds the length of the cirle.

        Args:
            No
        Returns:
            float or int: result..
        """
        r=self.r
        p=pi*r*2
        return p
x=Circle(2)
print(x.getLength())