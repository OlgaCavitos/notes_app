# def add(a,b):
#     print(f'{a=}')
#     print(f'{b=}')
#     result=a+b
#     return result
#
# result=add(5,3)
# print(result)
#
def introduce(name,age=0,city=''):
    print(f"My name is: {name}', and age:{age}, city:{city}")


introduce(age=25,name='Olya', city='Lviv')
introduce(name='Olya', age=39)
introduce(name='Olya',)
#
#
# def sum_all(*args):
#     print('args: ', args)
#     print('type(args): ' , type(args))
#     return sum(args)
#
# print(sum_all(1,4,5,3,9))
#
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"key: {key}, value: {value}")
#

#print_info(name='Olya', city='Lviv', email='testemail.com')

# def greeting(name: str,age: int=18):
#     print(f"Hello, {name}! You are {age} years old.")
# result=greeting('john',20)
# print(result)


def add_to_list(item, items=[]):
    items.append(item)
    return items

print(add_to_list(1))
print(add_to_list(2))
print(add_to_list(3))

def add_to_list_2(item, items=None):
    if items is None:
        items=[]
    items.append(item)
    return items

print(add_to_list_2(1))
print(add_to_list_2(2))
print(add_to_list_2(3))


lst=['1','2','3','4']

def lst_fnc(a,b):
    lst.append(a)
    lst.append(b)

print(lst)
lst_fnc(5,6)
print(lst)


#lamba function

#lambda аргумент: вираз

def mul(x,y):
    return x*y
print(mul(2,3))
mul_lambda=lambda a,b:a*b
print(mul_lambda(1,2))

pairs=[(1,"b"), (3,"a"), (5,"c")]
sorted_pairs = sorted(pairs, key=lambda x:x[1])   #x this is a tuple
print(sorted_pairs)

numbers=[1,2,3,4,5]
sq=list(map(lambda x: x**2, numbers))
print(sq)


x=50 #глобальна змінна

def func(x):
    print("x is :",x)
    x=2
    print('Changed local x to ', x)

func(x)
print('x is still: ', x)


x=50 #глобальна змінна

def func():
    global x
    print("x is :",x)
    x=2
    print('Changed local x to ', x)

func()
print('x is still: ', x)


def outer():
    x='local variable'

    def inner():
        nonlocal x
        x='local variable'
        print('inner function:',x)

    inner()
    print('outer function:',x)
outer()

def codes_of_string(string:str)->dict:
    codes={}
    for char in string:
        if not char in codes:
           codes[char]=ord(char)
    return codes

res=codes_of_string('hello')
print(res)



def make_country(name,capital):
    country_dict={name:capital}
    return country_dict
result_1=make_country('Romania','Bucharest')
print(result_1)

result_2=make_country('Ukraine','Kyiv')
print(result_2)


def make_country(name,capital):
    return {name:capital}

countries={}

countries.update(make_country('Romania','Bucharest'))
countries.update(make_country('Ukraine','Kyiv'))
countries.update(make_country('Germany','Berlin'))

print(countries)


