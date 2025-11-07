from _ast import arg


# def greeting(val):
#     print(f"My name is {val}")
#
#
# def greeting_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Hello')
#         result=func(*args, **kwargs)
#         print('bye bye')
#         return result
#     return wrapper
#
# change_greeting=greeting_decorator(greeting)
# change_greeting('Olya')


# def decorator_name(func):
#     def wrapper(name,surname):
#         print('decorator_name')
#         result=func(name, surname)
#         print('bye')
#         return result
#     return wrapper
#
# def prefixed_decorator(func):
#     def inner(name,surname):
#         print('start')
#         #decorator
#         #funct
#         #decorator
#         name=f"Mr {name}"
#         result=func(name,surname)
#         print('end')
#         return result
#     return inner
#
#
# @prefixed_decorator
# @decorator_name
#
# def full_name(name, surname):
#     print(f"Hello {name} {surname}")
#
# full_name("Joy", "Smith")


# def repeat_n_times(n):
#     #функція, яка буде приймати параметр n
#     def decorator(original_function):
#         #цу функціф, яка буде доповнювати оригінальну ф-цію
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 original_function(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat_n_times(3)
# def greet(name):
#     print(f"My name is {name}")
#
# greet('test')

# from time import time
# from functools import wraps
# from time import sleep
#
#
# def time_counter(func):
#     def interval(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         passed_time = time() - start
#         print(passed_time)
#         return result,passed_time
#     return interval
#
#
# @time_counter
# def test_func(a,b):
#     sleep(b)
#     return a+b
#
# print(test_func(1, 2))

# Створіть декоратор, який:
# - Логує початок і кінець виконання функції
# - Вимірює час виконання
# - Дозволяє задавати рівень логування (INFO, DEBUG, ERROR)
# - Зберігає логи у файл із часовою міткою

# import functools
# import time
# import logging
#
# def logger_1(level="INFO", logfile="logger"):
#     logging.basicConfig(filename=logfile, level=getattr(logging, level), format=('%(asctime)s - %(levelname)s - %(message)s'))
#     def logger_inner(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             logging.log(getattr(logging, level), f"Starting {func.__name__} with args: {args}, kwargs: {kwargs}")
#             try:
#                 result = func(*args, **kwargs)
#                 execution_time = time.time() - start_time
#                 logging.log(getattr(logging, level), f"Finished {func.__name__} in {execution_time} seconds.result:{result}")
#                 return result
#             except Exception as e:
#                 logging.error(f"Error in {func.__name__}: {e}")
#                 raise
#         return wrapper
#     return logger_inner
#
# @logger_1(level="DEBUG",logfile="calculation.log")
# def complex_calculaation(x,y,power=2):
#     time.sleep(1)
#     return x**power+y**power
#
# print(complex_calculaation(5,5))


# from functools import wraps
#
# def limit_calls(max_calls):
#     def decorator(func):
#         func.call_count=0  #зберігаємо кількість викликів як атрібут функції
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if func.call_count<max_calls:
#                 func.call_count += 1
#                 return func(*args, **kwargs)
#             else:
#                 return f"Error '{func.__name__}' has exceeded {max_calls} times."
#         return wrapper
#     return decorator
#
#
# @limit_calls(3)
# def say_hello(name):
#     return f'Hello, {name}!'
#
# print(say_hello('Michael'))
# print(say_hello('Lilia'))
# print(say_hello('Olivia'))
# print(say_hello('Misha')) #
# print(say_hello('Smith'))

# def my_decorator(func):
#     def wrapper():
#         print('before called function')
#         func()
#         print('after called function')
#     return wrapper
#
#
# @my_decorator
# def say_hello():
#     print('hello')
# say_hello()

# say_hello=my_decorator(say_hello)
# say_hello()

# def add_number(number):
#     return number+1
#
# print(add_number(2))

# def action_to_number(number):
#     def decorator(func):
#         def wrapper():
#             print(f"to return the function ({number})")
#             func(number)
#             return func
#         return wrapper
#     return decorator
#
# @action_to_number(10)
# def square_args(arg):
#     print(f"{arg}**2={arg**2}")
#
# square_func = square_args()
# print("Called :", square_func)


# def make_mult(f):
#     def mult(x):
#         return x * f
#     return mult
#
# dbl = make_mult(2)
# print(dbl(5))


# def outer():
#     message = "Hello, closure!"
#
#     def inner():
#         print(message)
#
#     return inner
#
#
# my_func = outer()
# my_func()


# def arg_rules(max_length=15, type_=str,contains=['1','0.2','@']):
#     def decorator(func):
#         if type_ in contains:
#             def wrapper():
#                 print(f"{func.__name__}({arg})")
#                 func(arg)
#
#
# def arg_rules(type_: type, max_length: int, contains: list):
#
#     pass



# words = ['apple', 'banana', 'cherry']
# res = map(lambda s: s[0], words)
# print(list(res))

# def plus_one(number):
#     return number + 1
#
# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)
#
# function_call(plus_one)
# print(function_call(plus_one))

# def outer_function(message):
#     def inner_function():
#         print(f"Message from closure: {message}")
#     return inner_function
#
# closure_function = outer_function("Hello, closures!")
# closure_function()
# # # Output: Message from closure: Hello, closures!


# def simple_decorator(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")
#     return wrapper
#
# @simple_decorator
# def greet():
#     print("Hello!")
#
# greet()


# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return wrapper


# def action_to_number(number):
#     def decorator(func):
#         def wrapper():
#             print(f"to return the function ({number})")
#             func(number)
#             return func
#         return wrapper
#     return decorator
#
# @action_to_number(10)
# def square_args(arg):
#     print(f"{arg}**2={arg**2}")
#
# square_func = square_args()
# if __name__=='__main__':
#     print("Called :", square_func)



# words=['cat','dog','lion','zebra']
# res=map(lambda s: s[0],words )
# print(list(res))

# words=['word','list','file', 'letter']
# res=map(lambda s: s[0],words)
# print((list(res)))


# words=['clock','time','file']
# res=map(lambda x: x[0], words)
# print(list(res))


# CHANNELS = ['BBC', 'Discovery', 'TV1000']
# print(CHANNELS[0])
# print(CHANNELS[1])
# print(CHANNELS[2])
# print(len(CHANNELS))
# print(CHANNELS[-1])
# print(CHANNELS[-2])
# print(CHANNELS[-3])

# class Employee:
#     emp_id=0
#
# emp_1=Employee()
# emp_2=Employee()
#
# emp_1.emp_id=1001
# emp_2.emp_id=1002
# print(f"EmployeeID: {emp_1.emp_id}")
# print(f"EmployeeID: {emp_2.emp_id}")

# a=[-3,4,5,-8,1,10]
# N=len(a)
#
# for i in range(1,N):
#     for j in range (i,0,-1):
#         if a[j] < a[j-1]:
#             a[j],a[j-1] = a[j-1],a[j]
#         else:
#             break
#
# print(a)


# def fibonacci(n):
#     if n <= 0:
#         return "Incorrect Output"
#     data = [0, 1]
#     if n > 2:
#         for i in range(2, n):
#             data.append(data[i-1] + data[i-2])
#     return data[n-1]
#
# print(fibonacci(10))

# s='gih5&'
# for char in s:print(char, char.isalpha())

# lst = [25, 12, 10, -21, 10, 100]
# indices = range(len(lst))
# for i in indices:
#    print ("lst[{}]: ".format(i), lst[i])

# import asyncio
# import random
#
# async def producer(queue):
#     for i in range(5):
#         item=random.randint(1,10)
#         await queue.put(item)
#         print(f"Producer: {item}")
#         await asyncio.sleep(1)
#
# async def consumer(queue, name):
#     while True:
#         item=await queue.get()
#         print(f"Consumer: {name} got {item}")
#         queue.task_done()
#         await asyncio.sleep(1)
#
#
# async def main():
#     queue=asyncio.Queue()
#     consumers = [asyncio.create_task(consumer(queue,i)) for i in range(2)]
#     await asyncio.gather(producer(queue), return_exceptions=True)
#
#     await queue.join()
#
#     for c in consumers:
#         c.cancel()
#
# asyncio.run(main())


#queue.put() - async adding to queue

#
# import asyncio
#
# async def handle_client(reader, writer):
#     """Handle a single client connection."""
#     addr = writer.get_extra_info("text")
#     print(f"Connection established with {addr}")
#
#     try:
#         while True:
#             data = await reader.read(1024)
#             if not data:
#                 print(f"Client {addr} disconnected")
#                 break
#
#             message = data.decode().strip()
#             print(f"Received from {addr}: {message}")
#
#             # Echo back the same data
#             writer.write(data)
#             await writer.drain()
#             print(f"Sent back to {addr}\n")
#
#     except ConnectionResetError:
#         print(f"Connection reset by {addr}")
#     finally:
#         writer.close()
#         await writer.wait_closed()
#         print(f"Connection closed with {addr}")
#
#
# async def main():
#     """Main coroutine to start the server and handle clients."""
#     host = input("Enter host to bind (default 127.0.0.1): ").strip() or "127.0.0.1"
#     port_input = input("Enter port to bind (default 65435): ").strip()
#     port = int(port_input) if port_input.isdigit() else 65435
#
#     server = await asyncio.start_server(handle_client, host, port)
#     addr = server.sockets[0].getsockname()
#     print(f"Asyncio Echo Server running on {addr}")
#
#     # Use asyncio Tasks to handle multiple connections concurrently
#     async with server:
#         await server.serve_forever()
#
#
# if __name__ == "__main__":
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("\nServer stopped manually.")

#
# import math
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# import time
# NUMBERS = [
#    2,  # prime
#    1099726899285419,
#    1570341764013157,  # prime
#    1637027521802551,  # prime
#    1880450821379411,  # prime
#    1893530391196711,  # prime
#    2447109360961063,  # prime
#    3,  # prime
#    2772290760589219,  # prime
#    3033700317376073,  # prime
#    4350190374376723,
#    4350190491008389,  # prime
#    4350190491008390,
#    4350222956688319,
#    2447120421950803,
#    5,  # prime
# ]
#
#
# # Utility function
# def is_prime(n: int) -> bool:
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#
#     limit = int(math.isqrt(n))
#     for i in range(5, limit + 1, 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#     return True
#
#
#
# #Concurrent Implementations
# def filter_primes_threadpool(numbers):
#     with ThreadPoolExecutor() as executor:
#         results = list(executor.map(is_prime, numbers))
#     return [num for num, prime in zip(numbers, results) if prime]
#
# def filter_primes_processpool(numbers):
#     with ProcessPoolExecutor() as executor:
#         results = list(executor.map(is_prime, numbers))
#     return [num for num, prime in zip(numbers, results) if prime]
#
#
# # Performance Comparison
# def main():
#     print("Filtering primes using ThreadPoolExecutor...")
#     start = time.perf_counter()
#     primes_threads = filter_primes_threadpool(NUMBERS)
#     end = time.perf_counter()
#     print(f"ThreadPoolExecutor primes: {primes_threads}")
#     print(f"Time taken (threads): {end - start:.2f} seconds\n")
#
#     print("Filtering primes using ProcessPoolExecutor...")
#     start = time.perf_counter()
#     primes_processes = filter_primes_processpool(NUMBERS)
#     end = time.perf_counter()
#     print(f"ProcessPoolExecutor primes: {primes_processes}")
#     print(f"Time taken for processes: {end - start:.2f} seconds\n")
#
#     # Verify results are identical
#     assert primes_threads == primes_processes, "Results differ!"
#
# if __name__ == "__main__":
#     main()

