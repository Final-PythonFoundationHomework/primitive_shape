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
        x1=self.x1
        y1=self.y1
        x2=self.x2
        y2=self.y2
        l=sqrt((x2-x1)**2+(y2-y1)**2)
        return l
x=Line(3,4,0,0)
print(x.get_length())