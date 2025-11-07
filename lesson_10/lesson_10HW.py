#Task 1

def oops():
    raise IndexError("IndexError exception")


def oops_1():
    try:
        oops()
    except IndexError as e:
        print(f"An exception of IndexError: {e}")

oops_1()


def oops_2():
    raise KeyError("Key error found")


def oops_2_1():
    try:
        oops_2()
    except KeyError as k:
        print(f"An exception of KeyError: {k}")

oops_2_1()


def oops_3():
    raise KeyError("Key error found")

def oops_3_1():
    try:
        oops_3()
    except IndexError as ie:
        print(f"An exception of IndexError: {ie}")

oops_3_1()


#Task2

def calculation_a_b():
    try:
        a=float(input('Please enter number a: '))
        b=float(input('Please enter number b: '))

        res=(a**2)/b
        return res

    except ValueError as ve:
        print("Enter a valid number", ve)
    except ZeroDivisionError:
         print("Cannot divide by zero")
    except Exception as e:
        print(f" The error is following: {e}")

operation=calculation_a_b()
print(f"Result of the operation: {operation}")