class Account:
    def __init__(self,bankname,name,number,balance):
       self.name=name
       self.number=number
       self.bankname=bankname
       self.balance=balance
    def deposit(self,amount):
       self.balance+=amount
       return f"Hello your current balance is {self.balance}"
    def withdraw(self,amount):
       self.balance-=amount  
       return f"Hello your current balance is {self.balance}" 