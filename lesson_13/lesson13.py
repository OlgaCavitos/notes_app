# import operator as op
#
# def foo():
#     s=4
#     d=5
#     f=4
#     return s+d+f
# print(foo())
# print(foo.__code__.co_nlocals)
#


# def some_function(x, y):
#     h = x + y
#     print("Number of local variables:", len(locals()))
#
# some_function(5, 10)
#


def _get_args_dict(fn, args, kwargs):
    args_names = fn.__code__.co_varnames[:fn.__code__.co_argcount]
    return {**dict(zip(args_names, args)), **kwargs}


def mult(a,b):
    return a*b

lst=[i for i in range(1,16)]

print(list(zip(lst[:-1],lst[1:])))

lst_str=[str(ele) for ele in lst]
lst_str_m=map(str,lst)
print(lst_str_m)
print(list(map(mult,lst[:-1],lst[1:])))

print(*lst)

print(list(map(lambda x: mult(*x), zip(lst[:-1],lst[1:]))))


# /  1  /  2  /3 4 5 6 7 8 9 10 11 12 13

print(' '.join(map(lambda x: f"|{x:^5d}",lst))+'|')

print(' '.join(map(lambda x: f"|{x:^5.2f}",lst))+'|')

print(' '.join(map("|{:^5d}".format,lst))+'|')


matrix =[[row*col for col in range(10)] for row in range(10)]
print(matrix)

print('\n'.join(map(lambda row: ' '.join(map(lambda x: f"|{x:^5d}",row))+'|',matrix)))

operations={'+': op.add,
            '-': op.sub,
            '*': op.mul, }


oper='+'
operations.get(oper)(10,20)
print(operations.get(oper)(10,20))

print(list(filter(lambda x: x%2 !=0,range(1,16))))

