# Task 1 - Number of local variables

def test_funct():
    s=4
    d=5
    f=4
    return s+d+f
print(f"Number of local variables:", test_funct.__code__.co_nlocals)

print()

#Task2 program to access a function inside a function


def factorial(x):
    result=1
    for i in range(1, x+1):
        result*=i
    return result

# for i in range(1,10):
#     print(str(i) + "!\t" + str(factorial(i)))

def factorial_range(start,end):
    factorials=[]
    for i in range(start, end -1,-1):
        factorials.append((i,factorial(i)))
    return factorials

factorials=factorial_range(9,1)
for i, fact in factorials:
    print(f"{i}!={fact}")
print()
#------------2 example--------------
def multiply(x,y):
    return x*y

def s_of_rectangle(width,height):
    return multiply(width,height)

print(f"The area of the rectangle will be equal to:", s_of_rectangle(10,15))
print()


# Task 3


def choose_func(nums: list, func1, func2):
    return func1(nums) if all(num > 0 for num in nums) else func2(nums)

def square_nums(nums):
    return list(map(lambda x: x ** 2, nums))

def remove_negatives(nums):
    return list(filter(lambda x: x > 0, nums))

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]


# print(choose_func(nums1, square_nums, remove_negatives))
# print(choose_func(nums2, square_nums, remove_negatives))