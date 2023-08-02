from math import sqrt
class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_length(self):
        """
        This method finds the length of line.

        Args:
            No
        Returns:
            float or int: distance.
        """
        if self.y2 == 0:
            return abs(self.x2) - abs(self.x1)
        if self.x2 == 0:
            return abs(self.y2) - abs(self.y1)
        if self.y2 != 0 and self.x2 != 0:
            return sqrt((abs(self.x2) - abs(self.x1)) + (abs(self.y2) - abs(self.y1)))
s = Line(30, 40, 50, 60)
print(s.get_length())