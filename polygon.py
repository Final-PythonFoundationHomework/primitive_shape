from math import sqrt
class Polygon:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def getArea(self):
        """
        This method finds the area of the Polygon.

        Args:
            No
        Returns:
            float or int: return Area of the polygon.
        """
        return (self.height*self.width)/2

    def getPerimeter(self):
        """
        This method finds the perimeter of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        return 2*sqrt(pow(self.width,2) + pow(self.height,2)) + self.width
# polygon = Polygon(3,5)
# print(polygon.getArea())
# print(polygon.getPerimeter())
# print(polygon.__class__)
# print(dir(polygon))