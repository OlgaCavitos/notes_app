# from errno import EOWNERDEAD
# from tty import ISPEED
# from enum import global_enum_repr


# class Animal:
#     def __init__(self, nickname:str, age:int)->None:
#         self.nickname = nickname
#         self.age = age
#
#
#     def get_info(self)->str:
#         return f"Nickname: {self.nickname}, Age: {self.age}"
#
#
#
# class Cat(Animal):
#     name=['Cat']
#
#     def __init__(self,nickname:str, age:int, owner:str)->None:
#         super().__init__(nickname,age)
#         self.owner=owner
#
#     def sound(self)->str:
#         return f"{self.nickname} sounds Meow!"
#
# cat=Cat("Simon", 4,"Olha")
# print(cat.nickname)
# print(cat.name)
# print(cat.sound())
# print(cat.get_info())
#
#
# cat_sec=Cat("Bob", 5,"Tim")
# # print(cat_sec.sound())
# cat.name[0]='Joe'
# print(f"cat_sec: {cat.name}")
# print(f"cat_sec: {cat_sec.name}")
# print(f'Cat name: {Cat.name}')
#
# class Transport:
#     def __init__(self, speed,capacity,fuel_type):
#         self.speed = speed
#         self.capacity = capacity
#         self.fuel_type = fuel_type
#
#     def move(self):
#         return f"{self.__class__.__name__} moves with speed {self.speed} km/h"
#
#     def stop(self):
#         return f"{self.__class__.__name__} stops"
#
#     def fuel_consumption(self):
#         return f"fuel consumption depends on type of transport"
#
#
#
# class Car(Transport):
#     def __init__(self, speed,capacity,fuel_type,num_doors):
#         super().__init__(speed,capacity,fuel_type)
#         self.num_doors = num_doors
#
#
#     def open_trunk(self):
#         return "Trunk is open"
#
#
# class Bus(Transport):
#     def __init__(self, speed,capacity,fuel_type,ticket_price):
#         super().__init__(speed,capacity,fuel_type)
#         self.ticket_price = ticket_price
#
#     def collect_fare(self, passengers):
#         return f"Collect fare for {passengers*self.ticket_price} hrn for race"
#
#     class Bicycle(Transport):
#         def __init__(self, speed,capacity,fuel_type,num_doors):
#             super().__init__(speed,capacity,fuel_type="No type")
#
#         def fuel_consumption(self):
#             return "Bicycle does not have fuel consumption"
#
#
# car=Car(5,5,"Car",1)
# bus=Bus(80,50,"Bicycle",2)
# bicycle=(30,)
#
# print(car.move(),bus.collect_fare(10))

# class LibraryItem:
#     def __init__(self, title, author,year):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.is_available = True
#
#
#     def borrow(self):
#         if self.is_available:
#             self.is_available = False
#             return f"{self.title} borrowed"
#
#         return f"{self.title} not available"
#
#     def return_item(self):
#         self.is_available = True
#         return f"{self.title} returned"
#
# class Book(LibraryItem):
#     def __init__(self, title, author, year,genre):
#         super().__init__(title,author,year)
#         self.genre=genre
#
#     def get_summary(self):
#         return f"{self.title}  by {self.author} on {self.year}"
#
# class Magazine(LibraryItem):
#     def __init__(self, title, author, year, issue_number):
#         super().__init__(title,author,year)
#         self.issue_number=issue_number
#
#     def get_issue_details(self):
#         return f"{self.title}  - {self.issue_number}"
#
#     class DVD(LibraryItem):
#         def __init__(self, title, author, year,duration, region_code):
#             super().__init__(title,author)
#             self.duration=duration
#             self.region_code=region_code
#
#
#         def play(self):
#             return f"{self.title} played {self.duration} {self.region_code}"
#
# magazine = Magazine("Magazine", "", "1999", "DVD")
# print(magazine.borrow())
# print(magazine.return_item())


# class BankAccount:
#     def __init__(self, account_number, balance, owner):
#         self.account_number = account_number
#         self.balance = balance
#         self.owner = owner
#
#     def deposit(self,amount):
#         self.balance += amount
#         return f"Deposited {amount} to {self.balance}"
#
#     def withdraw(self,amount):
#         if self.balance>= amount:
#             self.balance -= amount
#             return f"Withdrawed {amount} to {self.balance}"
#         return f" Not enough money"
#
#     def get_balance(self):
#         return f"The current balance: {self.balance}"
#
#
# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, balance, owner, interest_rate):
#         super().__init__(account_number, balance,owner)
#         self.interest_rate = interest_rate
#     def apply_interest(self):
#         self.balance+=self.interest_rate/100 * self.balance
#         return f"New Balance: {self.balance}"
#
# class CheckingAccount(BankAccount):
#     def __init__(self, account_number, balance, owner, overdraft_limit):
#         super().__init__(account_number,balance,owner)
#         self.overdraft_limit = overdraft_limit
#
#     def withdraw(self,amount):
#         if self.balance+self.overdraft_limit >= amount:
#             self.balance-=amount
#             return f"Withdrawed {amount} to {self.balance}"
#         return f"Not enough money"
#
# account=SavingsAccount('45623',2000,'Olya',15)
# print(account.get_balance())
# print(account.apply_interest())
# print(account.balance)
# print(account.withdraw(100))


# class Mathematician:
#     def square_nums(self, numbers:list[int]) -> list[int]:
#         return [i**2 for i in numbers]
#
#     def remove_positives(self, numbers:list[int]) -> list[int]:
#         return [i for i in numbers if i<=0]
#     def filter_leaps(self,years:list[int]) -> list[int]:
#         return [n for n in years if not((n%4==0 and n%100!=0) or (n%400==0))]
#
#
# if __name__ == '__main__':
#     math=Mathematician()
# print(math.square_nums([17, 11, 5, 4]))
# print(math.remove_positives([17, -11, -5, 4,-7]))
# print(math.filter_leaps([2001, 1884, 1995, 2003, 2020]))




#Task 1

# class Person:
#     def __init__(self, name:str, age:int, gender:str):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#
# class Student(Person):
#     def __init__(self, name: str, age: int, gender: str, student_id: str, grade: str, subjects: list):
#         super().__init__(name, age, gender)
#         self.student_id = student_id
#         self.grade = grade
#         self.subjects = subjects
#
#
# class Teacher(Person):
#     def __init__(self, name: str, age: int, gender: str, employee_id: str, salary: float, subjects_teaching: list):
#         super().__init__(name, age, gender)
#         self.employee_id = employee_id
#         self.salary = salary
#         self.subjects_teaching = subjects_teaching