# Counting Instances of a Class
class Counter:
 instances = 0
 def __init__(self):
   Counter.instances += 1
print(Counter.instances)
obj1 = Counter()
obj2 = Counter()
print(Counter.instances)
