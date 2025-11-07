#global
#nonlocal

# a=10
# b=20
# def foo():
#     b=50
#     def inner():
#         nonlocal b
#         global a
#         b*=2
#         a+=100
#         return a,b
#     return inner
#
#
#
# def counter():
#     x=0
#     def increment():
#         nonlocal x
#         x+=1
#         return x
#     return increment
#
#
#print(foo()())
#print(a,b)
#

# def greet():
#     return "Hello!"
#
# # Store the function in a variable
# say_hello = greet
#
# # Call the function using the variable
# print(say_hello())



# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with arguments: {args} and {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} returned: {result}")
#         return result
#     return wrapper
#
# @log_decorator
# def add(a, b):
#     return a + b
#
# add(3, 4)


# def some_function(x, y):
#     h = x + y
#     print("Number of local variables:", len(locals()))
#
# some_function(5, 10)


# words = ['apple', 'banana', 'cherry']

# def example_function():
#     a = 10
#     b = 20
#     c = 30
#     d = 40
#     print("Number of local variables:", len(locals()))  # This will print the number of local variables
#
# example_function()


# def example(a, b, c):
#     return a + b + c
#
# print(example.__code__)


# def greet(name):
#     return f"Hello, {name}!"
# def welcome_user(name):
#     greeting=greet(name)
#     print(greeting)
#
# welcome_user('Olya')


# def multiply(x,y):
#     return x*y
#
# def s_of_rectangle(width,height):
#     return multiply(width,height)
#
# print(f"The area of the rectangle will be equal to:", s_of_rectangle(10,15))


# def choose_func(nums: list, func1, func2):
#     pass

#
# def choose_func(nums: list, func1, func2):
#     if all(num > 0 for num in nums):
#         return func1(nums)
#     else:
#         return func2(nums)
#
# def square_nums(nums):
#     return list(map(lambda x: x ** 2, nums))
#
# def remove_negatives(nums):
#     return list(filter(lambda x: x > 0, nums))
#
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, -2, 3, -4, 5]
#
# assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
# assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
#
#
# print(choose_func(nums1, square_nums, remove_negatives))
# print(choose_func(nums2, square_nums, remove_negatives))