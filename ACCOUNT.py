class SBI:
  def __init__(self,account,balance=0):
    self.account=account
    self.balance=balance
  def deposite(self,amount):
    self.balance+=amount
    print(f"deposite:{amount},new balance:{self.balance}")
  def withdraw(self,amount):
    if amount<= self.balance:
      self.balance-=amount
      print(f"withdra:{amount},new balance:{self.balance}")
    else:
      print("not balance is present to withdraw")    
SBI1=SBI("1234")   
SBI1.withdraw(5000)
SBI1.deposite(6000)
