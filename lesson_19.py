# def sqr_generator(srat, stop):
#     for element in range(srat, stop):
#         yield element*element
#
#



# def main():
#     lst=[1,2,3,4,5]
#     lst2=[i for i in range(1,11)]
#     gen2=(i for i in range(1,11))
#     print(lst2)
#     print(gen2)
#     sqr_gen=sqr_generator(1,11)
#     for elem_2 in sqr_gen:
#         print(elem_2, end=' ')
#     print()
#
#     it=iter(lst2)
#     while True:
#         try:
#             element=next(it)
#             print(element*element)
#         except StopIteration as err:
#             break
#
#
# if __name__ == '__main__':
#     main()



def fib_generator(stop=10):
    current_fib, next_fib=0,1
    for _ in range(stop):
        fib=current_fib
        current_fib, next_fib = next_fib, current_fib + next_fib
        yield current_fib


def main():
    print(list(fib_generator()))

if __name__ == '__main__':
    main()