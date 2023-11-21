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
        return sqrt(pow(self.x2 - self.x1,2) + pow(self.y2 - self.y1,2))
lenth = Line(2,3,4,5)
print(lenth.get_length())