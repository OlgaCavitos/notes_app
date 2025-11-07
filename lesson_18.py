# class Circle:
#     def __init__(self,radius):
#         self._radius = radius
#
#     @property  #Getter       отримати значення
#     def radius(self):
#         return self._radius
#
#     @radius.setter  #встановити значення
#     def radius(self, value):
#         if value<0:
#             raise ValueError("Value must be positive")
#         self._radius = value
#
#     @radius.deleter
#     def radius(self):
#         print('Call')
#         del self._radius
#
# circle=Circle(4)
# print(circle.radius)
# circle.radius=5
# print(circle.radius)
# # circle.radius=-5
#
# del circle.radius


#
# class Animal:
#     def __init__(self,nickname,age, weight):
#         # self.__nickname=nickname
#         # self.__age=age
#         # self.__weight=weight
#
#         self.__nickname=None
#         self.__age=None
#         self.__weight=None
#         #setters will work
#         self.name=nickname
#         self.age=age
#         self.weight=weight
#
#
#     @property
#     def name(self):
#         return self.__nickname
#
#     @name.setter
#     def name(self, nickname):
#         if len(nickname)>0:
#             self.__nickname=nickname
#         else:
#             raise ValueError("Name cannot be empty")
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age=age
#
#     @property
#     def weight(self):
#         return self.__weight
#     @weight.setter
#     def weight(self, weight):
#         if weight>0:
#             self.__weight=weight
#         else:
#             raise ValueError("Weight must be greater than 0")
#
# class Turtle(Animal):
#     def __init__(self,nickname,age, weight):
#         super().__init__(nickname, age,weight)
#
#     @Animal.age.setter
#     def age(self,age):
#         if age in list(range(0,200)):
#             Animal.age.fset(self,age)
#         else:
#             raise ValueError("Age must be between 0 and 20")
#
#
#
# # cat=Animal('Milka', -5,0)
# # print(cat.name, cat.age, cat.weight)
# # print(cat.age)
# # cat.age=20
# turtle=Turtle("Julian",100,45)
# print(turtle.name)
# print(turtle.age)
# print(turtle.weight)

# def method_decorator(func):
#     def wrapper(self, *args):
#        print('---Decorator method run---')
#        result=func(self, *args)
#        print('---Decorator method run end---')
#        return result
#     return wrapper
#
#
# def class_decorator(cls):
#     print('---Decorator class run---')
#     new_cls=cls
#     new_cls.value=42
#     return new_cls
#
# @class_decorator
# class TestClass:
#     name="TestClass"
#
#     @method_decorator
#     def info(self,user):
#         return f" Hello {user}! This is {self.name}"
#
# t=TestClass()
# print(t.info('Olya'))
# print(t.value)
# t.test=10
# print(t.test)
#In:185
#{50:3,25:1,10:1}

# class Coin:
#     def __init__(self,number):
#         self.number=number
#         self._coins=(1,2,5,10,25,50)
#
#
#     def coins(self):
#         coins_data= {}
#         for i in self._coins[::-1]:
#             amount=self.number//i
#             coins_data[i]=amount
#             self.number-=i*amount
#         return coins_data
#
# more_coins=Coin(156)
# print(more_coins.coins())


# import re
# from functools import lru_cache
# from typing import Dict, Any
#
# class EmailValidator:
#     def __init__(self):
#         self._cache=Dict[str,str]={}
#     @staticmethod
#     @lru_cache(maxsize=100)
#     def _is_valid_email(email: str)->bool:
#         pattern=r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
#         return bool(re.match(pattern,email))
#
#     def __get__(self, obj, owner):
#         if obj is None:
#             return self
#         return self._cache[id(obj)]
#
#     def __set_name__(self, obj, value):
#         if not isinstance(value, str):
#             raise TypeError("Name must be a string")
#         if not self._is_valid_email(value):
#             raise ValueError("Email must be a valid email")
#
#         self._cache[id(obj)]=value
#
#
#     def __delete__(self, obj):
#         del self._cache[id(obj)]
#
# class User:
#     email=EmailValidator()
#
#     def __init__(self,email):
#         self.email=email
#
# user=User('correct@example.com')
# print(f" Valid email: {user.email}")
# try:
#     user_invalid=User('correctexample.com@')
#     print(f"Valid email:{user.email}")
#
# except ValueError as e:


# class UnitConvertor:
#     def __init__(self, unit_from, unit_to, conversation_factor):
#         self.unit_from = unit_from
#         self.unit_to = unit_to
#         self.conversation_factor = conversation_factor
#         self._values={}
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         else:
#             return self._values.get(id(instance))
#
#     def __set__(self, instance, value):
#         if not isinstance(value, (int,float)):
#             raise TypeError('Value must be an integer')
#         converted=value*self.conversation_factor
#         self._values[id(instance)] = converted
#
#     def __delete__(self, instance):
#         del self._values[id(instance)]
#
#
# class Temperature:
#     celsius=UnitConvertor('celsius', 'fahrenheit', 1.8)
#     def __init__(self, celsius):
#         self.celsius=celsius
#
#     @property
#     def farenheit(self):
#         return self.celsius+32
#
# temperature=Temperature(25)
# print(temperature.celsius)
# print(temperature.farenheit)


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self._counter=0

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, key):
        return self.tasks[key]

    def __setitem__(self, key, value):
        if not isinstance(value, dict) or "priority" not in value or "description" not in value:
            raise ValueError("The task must include priority and description")
        self.tasks[key] = value

    def __iter__(self):
        return iter(sorted(self.tasks.items(), key=lambda x: x[1]['priority'], reverse=True))

    def __contains__(self, key):
        return key in self.tasks

    def add_task(self,description, priority):
        self._counter+=1
        # self.tasks[self._counter] = {'description': description, 'priority': priority}
        self.tasks[self._counter] = {'description': description, 'priority': priority}
        return self._counter


task_manager = TaskManager()
task_id_1=task_manager.add_task("Do homework", 2)
task_id_2=task_manager.add_task("Check email", 2)

task_manager.tasks[5]="task"
task.manager[5]="word"

for task_id, task in task_manager:
    print (f"ID:{task_id}, priority:{task['priority']}, description:{task['description']}")
