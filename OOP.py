class Person:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def the_person(self):
        print(self.name, self.age, self.salary)


Floyd = Person("Floyd", 15, 36000)
Jeff = Person("Jeff", 22, 80000)

Floyd.the_person()
Jeff.the_person()
