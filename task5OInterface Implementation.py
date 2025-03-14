#Interface Implementation:
from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def method(self):
        pass

class Impl(Interface):
    def method(self):
        return "Method Implemented"

obj = Impl()
print(obj.method())

