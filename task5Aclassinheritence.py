#class inheritence
class Animal:
 def speak(self):
  return "Animal Sound"
class Dog(Animal):
 def speak(self):
  return "Bark"
dog = Dog()
print(dog.speak())
