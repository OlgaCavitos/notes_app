class Animal:
    counter = 0

    def __init__(self, name, age, sound=''):
        self.name = name
        self.set_age(age)  # Corrected: passing `age` directly here
        self.sound = sound
        self.__class__.counter += 1  # Increment counter for each instance created

    def set_age(self, new_age):
        if 1 <= new_age <= 20:
            self.__age = new_age
        else:
            raise ValueError('age must be between 1 and 20')

    def get_age(self):
        return self.__age

    def info(self):
        print(f"name: {self.name}, has age: {self.get_age()}")  # Changed self.age to self.get_age()

    def voice(self):
        print(f"{self.name} says {self.sound}")

    @staticmethod  # Corrected: method should be static as it is related to the class, not an instance
    def count(self):
        print(f"count = {self.__class__.counter}")

    def __str__(self):
        return f"{self.name} says {self.sound}"


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __repr__(self):
        return f"<{self.__class__.__name__} name={self.name}, age={self.get_age()}>"


    def __str__(self):
        return f"<{self.__class__.__name__}>{self.name}: says {self.get_age()}"
    def voice(self):
        pass

if __name__ == '__main__':
    cat = Animal('Kuzya', 1, 'Mur')  # Age should be an integer
    dog=Animal('Bob',1)
    try:
        cat.set_age(-10)
    except Exception as err:
        print(err)
    # cat.info()  # Now correctly calls info() method and prints details
    # cat.voice()  # Prints the sound of the cat

    print(cat)  # Prints cat's string representation

    # Access the count method
    # Animal.count()  # Prints the total count of Animal instances created

import math


class Fraction:
    def __init__(self, x, y):
        self.numerator = x
        self.denominator = y

        self.__simplify()

    def __simplify(self):
        gcd = math.gcd(x, y)

    def __add__(self, other):
        x = ...
        y = ...
        return self.__class__(x, y)

    def __mul__(self, other):
        x = ...
        y = ...
        return self.__class__(x, y)


if __name__ == '__main__':
    fraction_1 = Fraction(1, 2)
    fraction_2 = Fraction(2, 4)
    print(fraction_1)
