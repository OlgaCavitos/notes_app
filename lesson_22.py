#source file
#dictionary


#task: all words than do not included in the dictionary

#read dictionary

# read dictionary file n:
# dict=O(1) list=O(1)
# find=> O(n)
# to create generator
# read text file
  #readlinses
  #read line
  #split text
  #clean words
  # look word for in dict
##words=
#dictionary =set(word.lower() for word in words.words())
# for line  in file:
#   handle(line)

import math
from functools import cache
def call_logger(func):
    count=0
    def wrapper(arg):
        nonlocal count
        count+=1
        print(f"{count:>3} call function {func.__name__} ({arg})")
        #result=func(arg)
        return func(arg)
    return wrapper

@cache
@call_logger

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)



if __name__ == "__main__":
    print(fib(7))
    print(math.log2(6))
    print()
    print(fib(8))
    print()
    print(fib(9))



