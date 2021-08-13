class Person:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def the_person(self):
        print(self.name, self.age, self.salary)
