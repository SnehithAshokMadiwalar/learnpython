 #Multilevel Inheritance
class Grandparent:
  def feature(self):
    return "Feature from Grandparent"
class Parent(Grandparent):
  pass
class Child(Parent):
  pass
c = Child()
print(c.feature())
