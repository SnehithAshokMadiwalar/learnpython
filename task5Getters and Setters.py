#Getters and Setters
class Person:
 def __init__(self, name, age):
  self.__name = name

  self.__age = age
 def get_name(self):
   return self.__name
 def set_name(self, name):
   self.__name = name
p = Person("Alice", 25)
print(p.get_name())
p.set_name("Bob")
print(p.get_name())
