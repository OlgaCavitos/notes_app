class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property  # Getter
    def radius(self):
        return self._radius

    @radius.setter  # Setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius can"t be negative')
        self._radius = value

    @radius.deleter  # Deleter
    def radius(self):
        print('Call')
        del self._radius


circle = Circle(5)
print(circle.radius)
circle.radius = 7
print(circle.radius)
del circle.radius


