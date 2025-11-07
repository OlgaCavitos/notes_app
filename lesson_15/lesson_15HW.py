#Task 1
class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * self.age_factor

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
        print(f"Hello, my name is {self.first_name} {self.last_name} and I'm {self.age} years old")

if __name__=='__main__':
    person = Person("Olivia", "Smith", 18)
    person.called_talk()




#Task 3

class TVController:
    def __init__(self,channels:list[str]):
        self.channels = channels
        self.current_channel = 0

    def change_channel(self,step:int):
        self.current_channel=(self.current_channel+step) % len(self.channels)
        return self.channels[self.current_channel]

    def first_channel(self):
        self.current_channel = 0
        return self.channels[self.current_channel]

    def last_channel(self):
        self.current_channel = len(self.channels) - 1
        return self.channels[self.current_channel]

    def next_channel(self): return self.change_channel(1)
    def previous_channel(self): return self.change_channel(-1)

    def get_current_channel(self):
        return self.channels[self.current_channel]

    def exists(self, item):
        return "Yes" if(isinstance(item,int) and 1<= item <=len(self.channels)) or \
                       (isinstance(item,str) and item in self.channels) else "No"

    def turn_channel(self, n: int):
        if 1 <= n <= len(self.channels):
            self.current_channel = n - 1
            return self.channels[self.current_channel]
        else:
            return "No such a channel"

if __name__ == "__main__":
    channels = ['BBC', 'Discovery', 'TV1000']
    controller = TVController(channels)
    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.next_channel())
    print(controller.previous_channel())
    print(controller.get_current_channel())
    print(controller.turn_channel(2))
    print(controller.exists('TV1000'))
    print(controller.exists(4))
