#Polymorphism with Inheritance

class Bird:
  def fly(self):
     return "Bird can fly"
class Sparrow(Bird):
  def fly(self):
    return "Sparrow flies fast"
sparrow = Sparrow()
print(sparrow.fly())
