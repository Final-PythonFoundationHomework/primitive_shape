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
            float or int: return perimeter of the polygon.
        """
        if self.height > 0 and self.width > 0:
            return self.height * self.width
        return 0

    def getPerimeter(self):
        """
        This method finds the perimeter of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        if self.height > 0 and self.width > 0:
            return 2 * (self.height + self.width)
        return 0