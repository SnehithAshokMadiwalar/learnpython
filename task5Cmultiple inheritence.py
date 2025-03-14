 #Multiple Inheritance
class A:
  def method_A(self):
   return "Method from A"
class B:
  def method_B(self):
   return "Method from B"
class C(A, B):
  pass
obj = C()
print(obj.method_A(), obj.method_B())
