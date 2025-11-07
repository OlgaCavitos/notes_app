
#Task1 The greatest number
import random as rd
numbers=[rd.randint(1, 20) for _ in range(10)]
print("Random generated numbers:", numbers)
i=0
largest=numbers[0]

while i<len(numbers):
    if numbers[i]>largest:
        largest=numbers[i]
    i+=1
print("Largest number:", largest)



#Task 2 Exclusive common numbers.

import random as rd
list_1=[rd.randint(1, 10) for _ in range(10)]
print("Random generated numbers_list_1:", list_1)

list_2=[rd.randint(1, 10) for _ in range(10)]
print("Random generated numbers_list_2:", list_2)

common_list_3=[]
i=0
while i<len(list_1):
    if list_1[i] in list_2 and list_1[i] not in common_list_3:
       common_list_3.append(list_1[i])
    i+=1
print("list without duplicates:", common_list_3)

'''
common_numbers=list(set(list_1)&set(list_2))
print("Common numbers:", common_numbers) 
'''

#Task 3 Extracting numbers.


list_100=list(range(1,101))
print("List of numbers_100:", list_100)

new_list=[]
i=0
while i<len(list_100):
    if list_100[i]%7==0 and list_100[i]%5!=0:
        new_list.append(list_100[i])
    i+=1
print("List of numbers that are divisible by 7 but not a multiple of 5",new_list)