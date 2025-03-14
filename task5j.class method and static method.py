#class method and static method
class Example:
    count = 0
    
    def __init__(self):
        Example.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def static_method():
        return "This is a static method"
