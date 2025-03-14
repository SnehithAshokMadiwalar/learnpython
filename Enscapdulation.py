#Encapsulation
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

person = Person("John", 30)
person.set_name("Mike")
print(person.get_name())
