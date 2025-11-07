#Task 1

def some_function(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func
    return wrapper


@some_function
def add(x, y):
    return x + y

@some_function
def square(x):
    return x ** 2

if __name__ == '__main__':
    result_1 = add(1, 2)
    print(f"Print the function_1:{result_1}")

    result_2 = square(3)
    print(f"Print the function_2:{result_2}")



#Task 2
def stop_words(words:list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res=func(*args, **kwargs)
            for stop_word in words:
                res = res.replace(stop_word, "*"*len(stop_word))
            return res
        return wrapper
    return decorator



@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his new brand BMW!"

if __name__ == '__main__':
    assert create_slogan("Steve") == "Steve drinks ***** in his new brand ***!"
    print(create_slogan("Steve"))



#Task 3
def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, type_):
                print(f"Failed due to incorrect type {type_}")
                return False

            if len(arg) > max_length:
                print(f"Failed due to the length > max length {max_length}")
                return False

            for i in contains:
                if i not in arg:
                    print(f"Failed as it does not contain the required data type '{i}'")
                    return False
            return func(arg)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'