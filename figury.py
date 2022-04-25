import math

class Figure:
    def __init__(self):
        self._area = 1

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

class Circle(Figure):
    def __init__(self, rad=1):
        super().__init__()
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

    def __add__(self, other):
        return self.__class__(math.sqrt((self._area + other._area)/math.pi))

class Square(Figure):
    def __init__(self, sid=1):
        super().__init__()
        if sid < 0:
            self._side = 0
            print("Bok nie może być ujemny")
        else:
            self._side = sid
        self._area = self._side ** 2

    def __repr__(self):
        return f"Square ({self._side})"

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, val):
        if val < 0:
            self._side = 0
            print("Bok nie może być ujemny")
        else:
            self._side = val
        self._area = self._side ** 2

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
        self._side = math.sqrt(self._area)

    def __add__(self, other):
        return self.__class__(math.sqrt(self._area + other._area))

class Triangle(Figure):
    def __init__(self, sid=1, h=1):
        super().__init__()
        if sid < 0:
            self._side = 0
            print("Bok nie może być ujemny")
        else:
            self._side = sid
        if h < 0:
            self._height = 0
            print("Wysokość nie może być ujemna")
        else:
            self._height = h
        self._area = self._side * self._height / 2

    def __repr__(self):
        return f"Triangle ({self._side}, {self._height})"

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, val):
        if val < 0:
            self._side = 0
            print("Bok nie może być ujemny")
        else:
            self._side = val
        self._area = self._side * self._height / 2

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        if val < 0:
            self._height = 0
            print("Wysokość nie może być ujemna")
        else:
            self._height = val
        self._area = self._side * self._height / 2

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
        self._side = self._area/self._height/2

    def __add__(self, other):
        
        return self.__class__(self._area/2, 1)

# a = Circle()
# b = Circle(2)
#
# print(a.radius, a.area, a.diameter)
# print(b.radius, b.area, b.diameter)
# print(a)
# print(b)
# print(a+b)
#
# a.area=12.56637
# print(a.radius, a.area, a.diameter)



