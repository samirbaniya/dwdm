class Student:
    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address

    def display1(self):
        print(self.name)
        print(self.id)
        print(self.address)

class Teacher(Student):
    def __init__(self, name, id, address, salary):
        super().__init__(name, id, address)
        self.salary = salary

    def display(self):
        super().display1()
        print(self.salary)

# Example usage
obj = Teacher("Samir", 190, "Dhulikhel", 160000)
obj.display()
