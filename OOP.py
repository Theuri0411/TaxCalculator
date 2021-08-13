class Person:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary


Floyd = Person("Floyd", 15, 36000)
Jeff = Person("Jeff", 22, 80000)

print(Jeff.salary)
print(Floyd.age)
print(Jeff.name)