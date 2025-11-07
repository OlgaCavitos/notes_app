#our_first_list=[1,2,3]
#print(our_first_list)
#another_list=[1,2,0.1]
#print(another_list)

#our_first_tuple=(1,2,3)
#print(our_first_list)
#another_tuple=(1,2,0.1)
#print(another_list)
#print("Len of our first list:",len(our_first_list))
#print("Len of another list:",len(another_list))
#print("Max element in list:", max(our_first_list))
#print("Min element in list:", min(another_list))

#a=[0,0,1,2,2,3,4,7,9]
#res=set(a)
#print(res)
#print(list(res))

shopping_list = []
prices = [0, 25, 40, 30, 15] # ціни для товарів
print('shopping list:')
print(shopping_list)
print('prices:')
while True:
    print('===list of shopping items==')
    print('1.Add item')
    print('2.Display item')
    print('3.Calculate price')
    print('4.Exit')
    choice = input('Choose the option: ')
    if choice == '1':
        shopping_item = input('Enter the item: ')
        user_quantity = int(input('Enter the quantity: '))
        user_priority = int(input('Enter the priority from 1 to 5: '))
        if 1<=user_quantity<=5:
             shopping_list.append([shopping_item, user_quantity, user_priority])
        else:
            print('Invalid input')
    elif choice == '2':
        print(shopping_list)
    elif choice == '3':
        total=0
        pass
    elif choice == '4':
        break
