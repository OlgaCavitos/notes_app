#Task 3
from functools import wraps

class TypeDecorator:
    @staticmethod
    def to_type(current_type):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                result=func(*args, **kwargs)
                try:
                    return current_type(result)
                except (TypeError,ValueError):
                    raise ValueError(f"{current_type.__name__} is not a valid type")
            return wrapper
        return decorator

if __name__ == "__main__":
    @TypeDecorator.to_type(int)
    def get_number():
        return 5

    @TypeDecorator.to_type(float)
    def get_float():
        return 5.25
    @TypeDecorator.to_type(str)
    def get_list():
        return [1,2,3,4,5]

    @TypeDecorator.to_type(bool)
    def get_bool():
        return ""


    print(get_number())
    print(get_float())
    print(get_list())
    print(get_bool())




#Task 1
import re
class Validator:
    def __init__(self, email):
        self.email=email
        self.validate()

    def validate(self):
        pattern=r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
        if not re.match(pattern,self.email):
            raise ValueError("Invalid email format")
        return True

if __name__ == '__main__':
    e1=Validator("abc@mail.com")
    # e2=validate_email("abc.def@mail")

    print(e1.email)
    # print(e2.email)



#Task 2

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return tuple(self._workers)

    def add_worker(self, worker):
        if worker not in self._workers:
            self._workers.append(worker)
            worker.boss = self
        if not isinstance(worker, Worker):
            raise ValueError("Only Worker can be added")

    def __repr__(self):
        return f"Boss({self.id}, {self.name}, {self.company})"

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss=None):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        if boss is not None:
            self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if self._boss is not None and self in self._boss._workers:
            self._boss._workers.remove(self)
        self._boss=value
        if not isinstance(value, Boss):
            raise ValueError("Only Boss can be instance of Boss")
        if self not in value.workers:
            value._workers.append(self)

    def __repr__(self):
        return f"Worker({self.id}, {self.name}, {self.company})"


if __name__ == "__main__":
    boss_1=Boss(1, "Mark", "MIX")
    boss_2=Boss(2, "Tom", "BYD")

    worker_1=Worker(1, "Paul", "MIX", boss_1)
    worker_2=Worker(2, "Richard", "BYD",boss_2)
    boss_1.add_worker(worker_2)
    print(boss_1.workers)
    print(boss_2.workers)

    worker_1.boss = boss_2
    print(boss_1.workers)
    print(boss_2.workers)
    print(worker_1.boss)






