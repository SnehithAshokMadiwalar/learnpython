#Serialization with OOP
import pickle

class Data:
    def __init__(self, value):
        self.value = value
    
    def save(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
    
    @staticmethod
    def load(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)

data = Data(42)
data.save("data.pkl")
loaded_data = Data.load("data.pkl")
print(loaded_data.value)
