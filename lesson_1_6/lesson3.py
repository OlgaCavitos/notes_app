#Task1
name='Olya'
day='Today'
#print("Good day {name}! {day} is a perfect day to learn some python.")
print(f"Good day {name}! {day} is a perfect day to learn some python.")

template="Good day {}! {} is a perfect day to learn some python."
print(template.format(name,day))




#Task2
firstname='Olha'
lastname='Pavlova'
print(firstname,lastname,sep=" ")

print(firstname,lastname, sep=",")

print(firstname +' '+lastname)

fullname=firstname +' '+lastname
print(fullname)
template="Hello, {}!"
print(template.format(fullname))

#Task3
a=10
b=15
print(a+b)
print(a-b)
print(a/b)
print(b//a)
print(b%a)
print(a/a)
print(b*a)
print(a**b)
print(b**a)
t = pow(a, b)
print(t)
import math
division = b / a
result = math.floor(division)
print(result)

print('a=10','b=15','a+b='+str(a+b))
print(f", a:{a}+b:{b}={a+b}")