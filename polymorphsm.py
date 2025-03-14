#polymorphsm
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
  def __init__(self,length,width):
    self.length=length
    self.width=width

  def area(self):
    return self.length*self.width
class Circle(Shape): 
  def __init__(self,radius):
    self.radius=radius
  def area(self):
    return 3.14*self.radius*self.radius

circle=Circle(6)
rectangle=Rectangle(4,5)
print("area of circle",circle.area())
print("area of rectangle",rectangle.area())
