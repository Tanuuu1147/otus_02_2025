import math
from src.Figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle sides must be greater than zero")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("A triangle with these sides does not exist")

        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))