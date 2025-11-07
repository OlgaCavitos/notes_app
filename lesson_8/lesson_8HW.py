#Task1
def favorite_movie(name,year):
    print(f"My favorite movie is named {name}, year {year}")

favorite_movie(name='Inception', year=2010)


#Task 2 Creating a dictionary

countries={}
def make_country(name,capital):
    countries[name]=capital
    return countries

make_country('Ukraine','Kyiv')
make_country('Romania','Bucharest')
make_country('Poland','Warsaw')

print(countries)


#Task 3 A simple calculator.

def make_operation(operation,*numbers):
    if not numbers:
        return 0
    if operation == '+':
        result=0
        for n in numbers:
            result+=n
    elif operation == '-':
        result=numbers[0]
        for n in numbers[1:]:
            result-=n
    elif operation == '*':
        result=1
        for n in numbers:
            result*=n
    else:
        raise ValueError('Invalid operation')
    return result

print(make_operation('+',8,2))
print(make_operation('-',5,9))
print(make_operation('*',2,2))
