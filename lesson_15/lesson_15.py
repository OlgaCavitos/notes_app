
# def foo(a,b):
#     x=a
#     y=b
#     return x+y
# def test():
#
#     assert foo(2,3) == 5
#
#
# if __name__ == "__main__":
#     test()


# lst=[5,3,2,7]
# lst.sort()
# print(lst)


class Pet:
    # name='Noname'
    counter=0

    # age=0
    def __init__(self,name,age,sound=''):
        self.name=name
        self.age=age
        self.sound=sound
        Pet.counter+=1  #self.__class__.__name__

    def info(self):
        print(f"name:{self.name}, has age:{self.age}")

    def voice(self):
        print(f"{self.name} says {self.sound}")

    def count():
        print(f"count ={Pet.counter}")

if __name__=='__main__':
    cat=Pet('Milka','1','Mur')
    dog=Pet('Rex','2', 'Gav-gav')
    Pet.count()
    print("cat.counter=",cat.counter)
    print(cat.__dict__)
    # print(type(cat))
    # print(type(cat),cat)
    # cat.name='Milka'
    # dog.name='Rex'

    # print(cat.name)
    # print(dog.name)

    #Pet.info(cat) for understanding
    #Pet.info() #cat.infor()
    cat.info()
    dog.info()
    cat.voice()
    dog.voice()


    # class Contact:
    #     def __init__(self,firstname,lastname, numbers):
    #         self.firstname=firstname
    #         self.lastname=lastname
    #         self.numbers=numbers
    #         #self.set_full_name()
    #
    #
    #     def set_fullname(self, display_mode):
    #         if display_mode=="first_and_last":
    #             self.fullname=f"{self.firstname} {self.lastname}"
    #         elif display_mode=="last_coma_first":
    #             self.fullname=f"{self.firstname}, {self.lastname}"
    #
    #     def get_fullname(self, mode):
    #         self.set_fullname(mode)
    #         return self.fullname
    #
    #
    # # def input_contact():
    # #     first_name=input("Enter your first name: ")
    # #     last_name=input("Enter your last name: ")
    # #     numbers=input("Enter your numbers: ")
    #
    # contact=Contact("Bill","Murrey", "0934562381")
    # print(contact.get_fullname("first_and_last"))

#
#     class Car:
#         def __init__(self, make, model, year,color,speed):
#             self.make = make
#             self.model=model
#             self.year = year
#             self.color=color
#             self.started=False
#             self.speed=0
#             self.max_speed=200
#
#
#         def accelerate(self, value):
#             if not self.started:
#                 print("Car is not started!")
#                 return
#             if self.speed + value <= self.max_speed:
#                 self.speed += value
#             else:
#                 self.speed = self.max_speed
#             print(f"Accelerating to {self.speed} km/h...")
#
#         def brake(self, value):
#             if self.speed - value >= 0:
#                 self.speed -= value
#             else:
#                 self.speed = 0
#             print(f"Braking to {self.speed} km/h...")
#
# ford_mustang = Car("Ford", "Mustang", 2022, "Black","100")
# ford_mustang.brake(100)

#Task 1
class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * Dog.age_factor

dog = Dog(7)
if __name__=='__main__':
    print(f"The dog’s age in human equivalent: {dog.human_age()}")


#Task 2

class Person:

    def __init__(self, first_name,last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def called_talk(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I'm says {self.age} years old")

if __name__=='__main__':
    person = Person("Olivia", "Smith", 18)
    person.called_talk()