# sentence="Hello World"
# words={}
# for word in sentence.split():
#     words[word]=words.get(word,0)+1
#
# print(words)

# result=0
#
# try:
#     value_1 = int(input("Please set first value: "))
#     value_2 = int(input("Please set second value: "))
#     result=value_1/value_2
#     a=[]
#     print(a[500])
# except ZeroDivisionError:
#     print('You can\t divide by zero')
# except ValueError:
#     print('Please enter the number')
# except IndexError as e:
#     print(f'You can\t enter {e}')
#     print(type(e))
#
# print(result)


# result=0
#
# try:
#     value_1 = int(input("Please set first value: "))
#     value_2 = int(input("Please set second value: "))
#     result=value_1/value_2
# except ZeroDivisionError:
#     print('You can\'t divide by zero')
# else:
#     print(f'Result is:{result}')
# finally:
#     print('The end of calculation is')
# print(result)


# result=0
# try:
#     value_1 = int(input("Please set first value: "))
#     value_2 = int(input("Please set second value: "))
#     result=value_1/value_2
# except Exception as e:
#     print('Error is: ', e)
# else:
#     print('The result is: ', result)
# finally:
#     print('The end of calculation is: ', result)


# result=0
# try:
#     value_1 = int(input("Please set first value: "))
#     value_2 = int(input("Please set second value: "))
#     result=value_1/value_2
# except ZeroDivisionError:
#     print('Zero Division Error')
# except TypeError:
#     print('Type Error')
# except Exception as e:
#     print('Error is: ', e)

#
# def calculator():
#     try:
#         num1=float(input('Please enter first number: '))
#         num2=float(input('Please enter second number: '))
#         operation=input('Please enter operation: (+,-,*,/) ')
#
#         if operation=='+':
#             result=num1+num2
#         elif operation=='-':
#             result=num1-num2
#         elif operation=='*':
#             result=num1*num2
#         elif operation=='/':
#             result=num1/num2
#         else:
#            raise ValueError('Invalid operation')
#
#     except ZeroDivisionError:
#         print('Zero Division Error')
#     except ValueError as ve:
#         print('Type Error': {ve})
#     else:
#     print('Error is: ', result)


#dic_1={"Олег": 85, "Марія": 92, "Іван": 78, "Анна": 95}

# def get_student_grade():
#     students={"Олег": 85, "Марія": 92, "Іван": 78, "Анна": 95}
#     try:
#         user_name=input("Please enter user name: ")
#         grade=students[user_name]
#         print(f"Your grade is {grade} for the student {user_name}")
#
#     except KeyError:
#         print("There is no student with that name")
#     except Exception as e:
#         print("Something went wrong")

#
# def add_to_set():
#     numbers = {1,2,3,4,5}
#     try:
#         new_number=int(input("Enter a number to the set: "))
#         if new_number in numbers:
#             print(f'The {new_number} is already in the set')
#         else:
#             numbers.add(new_number)
#             print(f'The {new_number} is now in the set')
#     except ValueError:
#         print('Enter a valid number')
#     except Exception as ex:
#         print(f'Unknown error: {ex}')
#
# add_to_set()
#
# def calculate_average():
#     input_string=input("Enter the numbers:")
#     try:
#         numbers=[float(x) for x in input_string.split(",")]
#         if not numbers:
#             raise ValueError("List is empty")
#         aver=sum(numbers)/len(numbers)
#         print("The average is", aver)
#     except ValueError as e:
#         print("error", e)
#     except Exception as e:
#         print("Unknown Error")
#
# calculate_average()


# def calculation_a_b():
#     try:
#         a=float(input('Please enter number a: '))
#         b=float(input('Please enter number b: '))
#
#         res=(a**2)/b
#         return res
#
#     except ValueError as ve:
#         print("Value invalid error", ve)
#     except ZeroDivisionError:
#          print("Cannot divide by zero")
#     except Exception as e:
#         print(f" The error is following: {e}")
#
# operation=calculation_a_b()
# # if operation is not None:
# print(f"Result of the operation: {operation}")
#


# def oops():
#     print("Oops!")
# oops()

# some_text="Some text is added"
#
# def count_words(some_text):
#     words=some_text.split()
#     return len(words)
#
# count_word=count_words(some_text)
# print(f"Count words: {count_word}")

# some_text="Some text"
# def count_letters(some_text):
#     letters_1=[char for char in some_text if char.isalpha()]
#     return len(letters_1)
#
# letter_count=count_letters(some_text)
# print(f"The letter count: {letter_count} ")



# import sys
#
# print("the Path")
# for path in sys.path:
#     print(path)

#import os

# Current working directory
#my_dir = os.getcwd()
#print("Current Directory:", my_dir)

# s = 'a1中文'
# for char in s: print(char, char.isalpha())

# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
#
# @uppercase
# def greet():
#     return "Hello!"
#
# greet()

# def test_words(stop_words):
#     def decorator(func):
#         def wrapper(text):
#             text_1 = text
#             for stop_word in stop_words:
#                 text_1 = text_1.replace(stop_word, "*"*len(stop_word))
#             return func(text_1)
#         return wrapper
#     return decorator
#
#
#
# @test_words(['pepsi', 'BMW'])
# def text_display(some_text):
#     print(some_text)
#
# text_display(f"drinks pepsi in his brand new BMW!")
# text_display(f"pepsi is not a healthy drink")



# def decorator_with_arguments(function):
#     def wrapper_accepting_arguments(arg1, arg2):
#         print("My arguments are: {0}, {1}".format(arg1,arg2))
#         function(arg1, arg2)
#     return wrapper_accepting_arguments
#
#
# @decorator_with_arguments
# def cities(city_one, city_two):
#     print("Cities I love are {0} and {1}".format(city_one, city_two))
#
# cities("Nairobi", "Accra")


# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
#         print('The positional arguments are', args)
#         print('The keyword arguments are', kwargs)
#         function_to_decorate(*args)
#     return a_wrapper_accepting_arbitrary_arguments
#
# # @a_decorator_passing_arbitrary_arguments
# # def function_with_no_argument():
# #     print("No arguments here.")
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print(a, b, c)
#
# function_with_arguments(1,2,3)

# function_with_no_argument()


# isinstance(123,int)
# isinstance(123,str)

# s = 'a1中文'
# for char in s: print(char, char.isalpha())


# d='f4G%'
# for char in d: print(char, char.isalpha())

# f='h&*KL'
# for char in f: print(char, char.isalpha())

# words=['clock','time','file']
# res=map(lambda x: x[0], words)
# print(list(res))

# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took {end - start} seconds")
#         return result
#     return wrapper
#
# @timer
# def log_run_task():
#     time.sleep(2)

# class Dog:
#     age_factor = 7
#     height_factor=5
#
#     def __init__(self, dog_age, dog_height):
#         self.dog_age = dog_age
#         self.dog_height = dog_height
#
#     def human_age(self):
#         return self.dog_age * self.age_factor
#
#     def human_height(self):
#         return self.dog_height * self.height_factor
#
# dog = Dog(7,5)
#
# if __name__=='__main__':
#     print(f"The dog’s age in human equivalent: {dog.human_age()}")
#     print(f"The dog's height in human equivalent: {dog.human_height()}")



# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         result= func(*args, **kwargs)
#         print(f"Function {func.__name__} returned {result}")
#         return result
#     return wrapper
#
# @logger
# def add(x,y):
#     return x+y
#
# add(4,1)

# def admin_required(func):
#     def wrapper(user,*args, **kwargs):
#         if user!='admin':
#             raise Exception("This function requires admin rights")
#         return func(*args,**kwargs)
#     return wrapper
# @admin_required
# def delete_database():
#     print("Database has been deleted")
#
# delete_database('admin')
# delete_database('guest')


# class Phonebook:
#     def __init__(self):
#         self.book=[]
#
#     def add(self, contact):
#         if contact in self.book:
#             self.book.append(contact)
#
#     def __len__(self):
#         return len(self.book)

# import math
#
#
# class Fraction:
#     def __init__(self, x, y):
#         self.numerator = x
#         self.denominator = y
#
#
#         self.__simplify()
#     def __simplify(self):
#         gcd = math.gcd(x, y)
#
#
#     def __add__(self, other):
#         x=...
#         y=...
#         return self.__class__(x,y)
#
#
#     def __mul__(self, other):
#         x=...
#         y=...
#         return self.__class__(x,y)
#
# if __name__ == '__main__':
#     fraction_1 = Fraction(1,2)
#     fraction_2 = Fraction(2,4)
#     print(fraction_1)


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         x_new = self.x + other.x
#         y_new = self.y + other.y
#         return Vector(x_new, y_new)
#
#     def __call__(self):
#         return math.sqrt(self.x*)
#
#
#     def dot(self, other):
#         return self.x * other.x + self.y * other.y
#
#     def __mul__(self, magnitude):
#         self.x *= magnitude
#         self.y *= magnitude
#         return self
#
#     def __str__(self):
#         return f' Vector({self.x}, {self.y})'
#
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
# def test_vectors():
#     v1=Vector(1, 2)
#     v2=Vector(3, 4)
#     v3=v1+v2
#     v1==v2
#     print(v3)
#
#     print(v3*10)
#
#
#
# if __name__ == '__main__':
#     test_vectors()



# class CustomException(Exception):
#     def __init__(self, message):
#         super().__init__(message)  # Call base class constructor
#         self.message = message
#
#         # Log the error to a file
#         with open("logs.txt", "a") as log_file:
#             log_file.write(f"[CustomException] {self.message}\n")



# s='gih5&'
# for char in s:print(char, char.isalpha())
#
# words=['dog','cat','parrot']
# result=map(lambda x: x[0],words )
# print(list(result))
# words=['dog','cat','parrot']
# result=map(lambda x: x[-1],words )
# print(list(result))

#
# list_inst=[1,2,3,4,5]
# iterator=iter(list_inst)
# sorted_list=sorted(iterator,reverse=True)
# print(sorted_list)
#
# print(list(list_inst))

# celsius = [0, 20, 37, 100]
# fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
# print(list(fahrenheit))

#

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
#
# new_dict = {}
# for key in dict1:
#     if key in dict2:
#         new_dict[key] = dict1[key] + dict2[key]
#
# print(new_dict)


# import unittest
#
# def add(a, b):
#     return a + b
#
# class TestAddFunction(unittest.TestCase):
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(1, 2), 3)
#
#     def test_add_negative_numbers(self):
#         self.assertEqual(add(-1, -2), -3)
#
#     def test_add_mixed_numbers(self):
#         self.assertEqual(add(1, -2), -1)
#         self.assertEqual(add(-1, 2), 1)
#
# if __name__ == '__main__':
#     unittest.main()

#
# class MyContext:
#     def __enter__(self):
#         print("Entering context")
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting context")
#
# ctx = MyContext()
# ctx.__enter__()
#
# try:
#     print("Doing some work manually")
# finally:
#     ctx.__exit__(None, None, None)

#


# class MyContext:
#     def __enter__(self):
#         print("Entering context")
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting context")
#         if exc_type:
#             print(f"An exception occurred: {exc_type.__name__} - {exc_value}")
#         return True  # Suppresses the exception
#
# # Use the context manager
# with MyContext():
#     print("About to divide by zero...")
#
#     print("This will not print")

#
# my_list=[4,5,6,45,8]
# def find_max(my_list):
#     my_max = my_list[0]
#     for item in range(len(my_list)):
#         if my_list[item] > my_max:
#             my_max = my_list[item]
#     return my_max
#
# def find_min(my_list):
#     my_min = my_list[0]
#     for item in range(len(my_list)):
#         if my_list[item] < my_min:
#             my_min = my_list[item]
#     return my_min
#
#
# print(find_max(my_list))
# print(find_min(my_list))

# def fact2(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact2(n-1)
#
# print(fact2(5))


#
# k = 0
# for i in range(10):
# 	for j in range(5):
# 		k = k + i
# print(k)

# from typing import List, Tuple
#
# def question5(n: int) -> List[Tuple[int, int]]:
#     res: List[Tuple[int, int]] = []
#     for i in range(n):
#         for j in range(n):
#             res.append((i, j))
#     return res
#
# print(question5(3))




