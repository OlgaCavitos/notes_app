#Task 3

from math import gcd

class Fraction:
    def __init__(self, x, y):
        if y==0:
            raise ValueError ("Denominator cannot be zero")
        self.numerator = x
        self.denominator = y
        self.simplify()

    def simplify(self):
        if self.numerator == 0:
            self.denominator = 1
            return self

        if self.denominator < 0:
            self.numerator, self.denominator = -self.numerator, -self.denominator

        greatest_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= greatest_divisor
        self.denominator //= greatest_divisor
        return self

    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"({self.numerator},{self.denominator})"

    def __add__(self, other):
        numerator = self.numerator*other.denominator+other.numerator*self.denominator
        denominator = self.denominator*other.denominator
        return Fraction(numerator, denominator)
    def __sub__(self, other):
        numerator = self.numerator*other.denominator-other.numerator*self.denominator
        denominator = self.denominator*other.denominator
        return Fraction(numerator, denominator)
    def __mul__(self, other):
        numerator = self.numerator*other.numerator
        denominator = self.denominator*other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a fraction with a numerator of zero")

        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)


    def __eq__(self, other):return (self.numerator, self.denominator)==(other.numerator,other.denominator)
    def __lt__(self, other):return self.numerator * other.denumerator < other.numerator * self.denominator
    def __le__(self, other):return self<other or self==other
    def __gt__(self, other):return not self<=other
    def __ge__(self, other):return not self>=other
    def __ne__(self, other):return not self==other

if __name__ == "__main__":
    fr1 = Fraction(4,8)
    fr2 = Fraction(2,4)
    fr3 = Fraction(1,4)

    print(f" Fraction:",fr1)
    print(f" Fraction:",fr2)
    print(f" Fraction:",fr3)

    print(f" Sum of fraction:",fr1+fr2)
    print(f" Difference of fraction:",fr2-fr3)
    print(f" Multiplication of fractions:",fr1*fr2)
    print(f" Division of fractions:", fr1/fr2)

print('\n')

#Task 1

class Animal:
    def talk(self):
        raise NotImplementedError("Subclasses should implement talk()")

class Dog(Animal):
    def talk(self):
        return "woof"

class Cat(Animal):
    def talk(self):
        return "meow"

def animal_talk(animal: Animal):
    print(animal.talk())

if __name__ == '__main__':
    animals=[Dog(),Cat(),Dog(), Cat()]
    for i in animals:
        animal_talk(i)

print('\n')

#Task 2
class Author:
    def __init__(self, name:str,country:str, birthday:str):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books=[]

    def __str__(self):
        return f"{self.name} ({self.country} and was born {self.birthday})"
    def __repr__(self):
        return f"Author(name= {self.name}, country= {self.country},birthday={self.birthday})"


class Book:
    counter_book=0

    def __init__(self, name: str, year: int, author: Author):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")

        self.name = name
        self.year = year
        self.author = author
        Book.counter_book += 1
        author.books.append(self)

    def __str__(self):
        return f"'{self.name}' by {self.author.name} ({self.year})"

    def __repr__(self):
        return f"Book(name={self.name}, year={self.year}, author={self.author.name})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
        self.books_by_year={}

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)

        if author not in self.authors:
            self.authors.append(author)

        if year not in self.books_by_year:
            self.books_by_year[year] = []
        self.books_by_year[year].append(book)

        return book

    def group_by_author(self, author: Author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return self.books_by_year.get(year,[])

    def __str__(self):
        return f"Library: {self.name}, ({len(self.books)} books, {len(self.authors)} authors)"

    def __repr__(self):
        return f"Library(name={self.name}, books={len(self.books)}, authors={len(self.authors)})"


if __name__ == "__main__":
    author1 = Author("James Joyce", "UK", "1882-02-02")
    author2 = Author("Oscar Wilde", "UK", "1854-10-16")


    library_list=Library("Current Library")

    library_list.new_book(" Dubliners",1914,author2)
    library_list.new_book("The Harlot's House",1885,author1)

    print(library_list)
    print("Total number of books:", Book.counter_book)
    print("Filter by year:",library_list.group_by_year(1914) )
    print("Filter by author:",library_list.group_by_author(author1))
