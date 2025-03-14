#Multiple Inheritence
class Boy:
    def vishu(self):
       print("I am boy")
class Girl:
     def ishu(self):
       print("I am girl")
class Others(Boy,Girl):     
     def YOU(self):
       print("You are others")
Others1=Others()
Others1.ishu()
Others1.vishu()
Others1.YOU()
