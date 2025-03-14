#Exception Handling in Classes
class SafeDivision:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

obj = SafeDivision()
print(obj.divide(10, 2))
print(obj.divide(10, 0))
