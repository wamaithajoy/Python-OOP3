
class Account:
    def __init__(self,bankname,name,number):
       self.name=name
       self.number=number
       self.bankname=bankname
       self.balance=0
       self.deposits=[]
       self.withdrawals=[]
    def deposit(self,amount):
        
        if amount<=0:
            return f"Deposit must be a positive number"
        else:    
         self.balance+=amount
         self.deposits.append(amount)
        return f"Hello {self.name} your current balance is {self.balance}"
    def withdraw(self,amount):
        if amount<=self.balance and amount>0:
          transaction=amount+100
          self.balance-=transaction 
          self.withdrawals.append(amount)
        else:
            return f"You cant withdraw!! "  
        return f"Hello you have withdrawn {amount} and your current balance is {self.balance}"
    def deposits_statements(self):
        for x in self.deposits:
            print(f"Hello you have deposited {x}" ,end="\n")

    def withdrawals_statement(self):
        for x in self.withdrawals:
            print(f"Hello you have withdrawn {x}" ,end="\n")
    def current_balance(self):
        return f"Hello your current balance is {self.balance} "        

    

