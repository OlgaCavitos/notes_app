
#Task 1 The Guessing Game.

import random as rd
guess_number = rd.randint(1, 10)
guess=int(input("Guess a number between 1 and 10:"))
if guess == guess_number:
    print(f"You guessed right the number is {guess_number}")
else:
    print(f"You guessed {guess} wrong, the number is {guess_number}")



#Task 2 The birthday greeting program.

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(f"Hello {name}, on your next birthday you’ll be {age+1} years")


#Task3 Words combination
import itertools as it
world="hello"
permutations=it.permutations(world)
for perm in permutations:
    print("".join(perm))