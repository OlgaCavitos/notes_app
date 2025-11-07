class Animal:
    def __init__(self, nickname, age, weight):
        # self.__nickname = nickname
        # self.__age = age
        # self.__weight = weight
        self.__nickname = None
        self.__age = None
        self.__weight = None
        # сеттери спрацють
        self.name = nickname
        self.age = age
        self.weight = weight

    @property
    def name(self):
        return self.__nickname

    @name.setter
    def name(self, nickname):
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError("Тварини повинні мати ім'я")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Тварини повинні мати вагу!")


class Turtle(Animal):
    def __init__(self, nickname, age, weight):
        super().__init__(nickname, age, weight)

    @Animal.age.setter
    def age(self, age):
        if age in list(range(0, 200)):
            Animal.age.fset(self, age)
            # super(Turtle, type(self)).age.fset(self, age)
        else:
            raise ValueError('BAD')


# # cat = Animal('Boris', -15, 0)
# print(cat.name, cat.age, cat.weight)
# # cat.age = -5
# print(cat.name, cat.age, cat.weight)

turtle = Turtle("Turtila", 150, 100)
print(turtle.name, turtle.age, turtle.weight)
