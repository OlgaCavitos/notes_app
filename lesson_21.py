#
# from decimal import Decimal, localcontext, ROUND_HALF_UP
#
#
#
# def test_files():
#     file=None
#     try:
#         file=open("new_file1.txt","w")
#         file.write("Our first line is")
#     except:
#         print("Something went wrong")
#     finally:
#         if file is not None:
#             file.close()
#     try:
#         with open("new_file1.txt","w") as file:
#             file.write("Our second line is")
#     except:
#         print("Something went wrong")
#
# def test_with_decimal():
#     with localcontext(prec=4, rounding=ROUND_HALF_UP) as context:
#         result=Decimal("1")/Decimal("420")
#     print("Result division=", result)
#
#
#
# def main():
#     #test_files()
#     test_with_decimal()
#
# if __name__ == '__main__':
#     main()
#
#
# class Timer():
#     def working_with_list(lst):
#         k=3
#         while len(lst) >1:
#             for i in range(k-1):
#                 lst.append(lst.pop(0))
#                 lst.pop(0)
#                 return lst[0]
#
# def test_timer():
#     lst=[i for i in range(1,10000+1)]
#     with Timer():
#
# def main():
#         working_with_list(lst)
