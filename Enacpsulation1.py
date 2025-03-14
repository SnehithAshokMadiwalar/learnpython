#Encapsulation
class Apple:
    def __init__(self):
      self.public="red"
      self.__private="green"
    def get_green(self):
       return self.__private
Apple1 = Apple()

print(Apple1.public)  
print(Apple1.get_green())
