# Dunder Methods
class Sample:
 def __init__(self, name):
   self.name = name
 def __str__(self):
   return f"Name: {self.name}"
 def __repr__(self):
   return f"Sample('{self.name}')"
obj = Sample("John")
print(obj)
print(repr(obj))
