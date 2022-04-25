import math

class Figure:
    pass

class Circle:
    def __init__(self, rad=1):
        if rad < 0:
            self._radius = 0
            print("Promień nie może być ujemny")
        else:
            self._radius = rad
        self._area = self._radius*self._radius*math.pi
        self._diameter = self._radius *2

    def __repr__(self):
        return f"Circle ({self._radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            self._radius = 0
            print("Promień nie może być ujemny")
        else:
            self._radius = val
        self._area = self._radius*self._radius*math.pi
        self._diameter = self._radius *2

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, val):
        if val < 0:
            self._area = 0
            print("Pole nie może być ujemne")
        else:
            self._area = val
        self._radius = math. sqrt(self._area/math.pi)
        self._diameter = self._radius * 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, val):
        if val < 0:
            self._diameter = 0
            print("Średnica nie może być ujemna")
        else:
            self._diameter = val
        self._radius = self._diameter /2
        self._area = self._radius * self._radius * math.pi

    def __eq__(self, other):
        return self._area == other._area

    def __ne__(self, other):
        return self._area != other._area

    def __ge__(self, other):
        return self._area >= other._area

    def __le__(self, other):
        return self._area <= other._area

    def __gt__(self, other):
        return self._area > other._area

    def __lt__(self, other):
        return self._area < other._area

    def __add__(self, other):
        return self.__class__(math.sqrt((self._area + other._area)/math.pi))

a = Circle()
b = Circle(2)

print(a.radius, a.area, a.diameter)
print(b.radius, b.area, b.diameter)
print(a)
print(b)
print(a+b)

a.area=12.56637
print(a.radius, a.area, a.diameter)



