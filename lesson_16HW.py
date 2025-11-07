
#Task 2
print('Task_2')
class Mathematician:
    @staticmethod
    def square_nums(numbers:list[int]) -> list[int]:
        return [i**2 for i in numbers]

    @staticmethod
    def remove_positives(numbers:list[int]) -> list[int]:
        return [i for i in numbers if i<=0]

    @staticmethod
    def filter_leaps(years:list[int]) -> list[int]:
        return [year for year in years if not((year%4==0 and year%100!=0) or (year%400==0))]


if __name__ == '__main__':
    math=Mathematician()
    print(f" To reflect square nums:",math.square_nums([17, 11, 5, 4]))
    print(f" To remove positives:", math.remove_positives([17, -11, -5, 4,-7]))
    print(f" To display the list without leap years:", math.filter_leaps([2001, 1884, 1995, 2003, 2020, 2024]))

print('\n')

#Task 1
print('Task 1')
print('\n')

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name: {self.name}, and I'm: {self.age} years old"

    def get_role(self):
        return self.__class__.__name__


class Student(Person):
    def __init__(self, name, age, grade, group, subjects,phone_number):
        super().__init__(name, age)
        self.grade = grade
        self.subjects = subjects
        self.group=group
        self.phone_number=phone_number

    def get_student_group(self):
        return f"Student {self.name} and age of {self.age} is studying in {self.group}"

    def get_student_details(self):
        return (f"Student {self.name}, Group: {self.group}, Grade: {self.grade}, "
                f"Subjects: {', '.join(self.subjects)}, Phone Number: {self.phone_number}")

    def get_scholarship(self):
        if self.grade >= 4:
            return f"Student {self.name} with grade {self.grade} will receive the scholarship"
        return f"Student {self.name} with grade {self.grade} will not receive the scholarship"

class Teacher(Person):
    def __init__(self, name, age, salary, subject,experience):
        super().__init__(name, age)
        self.salary = float(salary)
        self.subject = subject
        self.experience = int(experience)

    def get_teacher_subject(self):
        return f"Teacher {self.name}, and age of {self.age} is teaching subject {self.subject}"

    def get_teacher_details(self):
        return (f"Teacher {self.name} ," 
                f" Subject:{self.subject} has Experience: {self.experience} years" 
                f" Salary: {self.salary}")
    def salary_increase(self, percent_increase: float = 5.0) -> float:
        increase = self.salary * (percent_increase/100)*self.experience
        self.salary+=increase
        return f'New salary increase for {self.name}: ${self.salary:.5f}'

if __name__ == "__main__":
    teacher=Teacher("Robin", "35","2000","Math","5")
    print(teacher.greet())
    print("Role:",teacher.get_role())
    print(teacher.get_teacher_subject())
    print(teacher.get_teacher_details())
    print(teacher.salary_increase())


    print('\n')
    print("Student section")

    student1=Student("Tom", 18,4,"A1",["Math", "Philosophy","Biology"],"+42502364223")
    student2=Student("Bill", 19,3,"A2",["Physics","Sociology","Math"],"+42503614892")

    print(student1.greet())
    print("Role:",student1.get_role())
    print(student1.get_student_group())
    print(student1.get_student_details())
    print(student1.get_scholarship())

    print('\n')

    print(student2.greet())
    print("Role:",student2.get_role())
    print(student2.get_student_group())
    print(student2.get_student_details())
    print(student2.get_scholarship())

print('\n')
#Task 3
print('Task_3')
print('\n')

class Product:
    def __init__(self, type_product, name, price):
        self.name = name
        self.type_product = type_product
        self.price = price

    def __str__(self):
        return f"Name: {self.name} ({self.type_product})- {self.price:.2f}"

    def __repr__(self):
        return f"Product(name='{self.name}', Type='{self.type_product}', Price='{self.price:.2f}')"


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0.0

    def add_product(self, product, amount):
        if amount < 0:
            raise ValueError("Amount must be more than 0")

        product_copy = Product(
            product.type_product,
            product.name,
            product.price * 1.3
        )

        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {'product': product_copy, 'amount': amount}

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent < 0 or percent > 100:
            raise ValueError("Discount % should be between 0 and 100")

        if identifier_type not in ['name', 'type']:
            raise ValueError("identifier_type must be 'name' or 'type' ")

        for product_data in self.products.values():
            product = product_data['product']
            if (identifier_type == 'name' and product.name == identifier) or \
               (identifier_type == 'type' and product.type_product == identifier):
                product.price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' is not available in the store")

        product_data = self.products[product_name]
        if product_data['amount'] < amount:
            raise ValueError(f"Not enough {product_name} in store to sell {amount} units")

        product_data['amount'] -= amount
        self.income += product_data['product'].price * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(product_data['product'].name, product_data['amount']) for product_data in self.products.values()]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' is not available in the store")

        product_data = self.products[product_name]
        return (product_name, product_data['amount'])


if __name__ == "__main__":
    product_1 = Product("Toys", "Bear", 50)
    product_2 = Product("Electronics", "Game console", 500)

    store = ProductStore()
    store.add_product(product_1, 100)
    store.add_product(product_2, 200)

    store.set_discount("Toys", 5, identifier_type="type")
    store.set_discount("Electronics", 15, identifier_type="type")

    store.sell_product("Bear", 3)

    print(f"Total Income: ${store.get_income():.2f}")
    print(f"Total Products: {store.get_all_products()}")
    print(f"Product details: {store.get_product_info('Game console')}")


print('\n')
print('Task_4')
print('\n')
#Task 4

class CustomException(Exception):
    def __init__(self, message:str):
        super().__init__(message)
        self.message = message
        self._log_to_file()

    def _log_to_file(self):
        with open("logs_1.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"[CustomException] {self.message}\n")

if __name__ == '__main__':
    try:
        raise CustomException("Something went wrong")
    except CustomException as e:
        print(f" exception: {e}")
    try:
        raise CustomException("Something went wrong again")
    except CustomException:
        pass

    print("Chek data in logs_1.txt")