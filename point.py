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
        return abs(self.y)

    def distance_from_Ycoordinate(self):
        """
        This method finds the distance between a point and its Y coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return abs(self.x)

    def getQuadrant(self):
        """
        This method finds which quadrant the point is in.

        Args:
            No
        Returns:
            int: quadrant.
        """
        if self.x > 0 and self.y > 0:
            return "1st quarter"
        if self.x < 0 and self.y > 0:
            return "2st quarter"
        if self.x < 0 and self.y < 0:
            return "3st quarter"
        if self.x > 0 and self.y < 0:
            return "4st quarter"

    def on_Xcoordinate(self):
        """
        This method checks for a point on the X coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        if self.y1 == 0 and self.y2 == 0:
            return "point is on the X-axis"
        

    def on_Ycoordinate(self):
        """
        This method checks for a point on the Y coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        if self.x1 == 0 and self.x2 == 0:
            return "point is on the Y-axis"
 