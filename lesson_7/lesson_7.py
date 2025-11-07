
#Task1
some_sentence = input("Please enter some_sentence: ")

#to split words
words= some_sentence.split()

#dictionary to create
counts={}
for word in words:
    word=word.lower().strip(",.?")
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
print("Initial count:", counts)

sorted_by_word=dict(sorted(counts.items()))
print("Sorted alphabetically:", sorted_by_word)

sorted_by_frequency = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
print("Sorted by frequency:", sorted_by_frequency)




#Task 2 --- Compute the total price---
#Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price={}
for item in stock:
    total_price[item] = stock[item] * prices[item]
print(f"Total_price: ",total_price)


total_price_list = dict(sorted(total_price.items()))
print("Sorted alphabetically:", total_price_list)

stock_list_frequency = dict(sorted(stock.items(), key=lambda item: item[1], reverse=True))
print("Sorted by frequency:", stock_list_frequency)




#Task 4 ---list of days of the week---

import calendar as cl
days=list(cl.day_name)

days_week_numbers = {i+1:days[i] for i in range(len(days))}
print(days_week_numbers)

numbers_days_weekday = {days[i]:i+1 for i in range(len(days))}
print(numbers_days_weekday)



#Task 3 list comprehension
res_2=[(el_i,el_i**2) for el_i in range(1,11)]
print(f"list containing tuples: {res_2}")

