from math import sqrt
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance_from_Xcoordinate(self):
        """
        This method finds the distance between a point and its X coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return "I chorak" if self.x > 0 and self.y > 0 else "II chorak" if self.x < 0 and self.y > 0 else "III chorak" if self.x < 0 and self.y < 0 else "IV chorak"

    def distance_from_Ycoordinate(self):
        """
        This method finds the distance between a point and its Y coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return self.x

    def getQuadrant(self):
        """
        This method finds which quadrant the point is in.

        Args:
            No
        Returns:
            int: quadrant.
        """
        return sqrt(pow(self.x,2) + pow(self.y,2))

    def on_Xcoordinate(self):
        """
        This method checks for a point on the X coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        return "nuqta x o\'qda joylashgan" if self.y==0 else "nuqta x o\'qda joylashmagan"

    def on_Ycoordinate(self):
        """
        This method checks for a point on the Y coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        return "nuqta y o\'qda joylashgan" if self.x==0 else "nuqta y o\'qda joylashmagan"
point = Point(2,0)
print(point.distance_from_Xcoordinate())
print(point.distance_from_Ycoordinate())
print(point.getQuadrant())
print(point.on_Xcoordinate())
print(point.on_Ycoordinate())