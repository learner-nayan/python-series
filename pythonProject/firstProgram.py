class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getstate__(self):
        return self.name


class Student(User):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address


object1 = User("John", 22)
object2 = Student("Ram", 21, "Damak")

# print(object1)
print(object1.__getstate__())
# print(object2)
