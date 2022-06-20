
from time import strftime


class Account:
    def __init__(self,bankname,name,number):
       self.name=name
       self.number=number
       self.bankname=bankname
       self.balance=0
       self.deposits=[]
       self.withdrawals=[]
       self.loan_balance=0
       self.my_balance=0

    def deposit(self,amount):
        
        if amount<=0:
            return f"Deposit must be a positive number"
        else:    
         self.balance+=amount
         self.deposits.append(amount)
         details={"Date":strftime("%d/%m/%y %H:%M:%S")}
         print(details)
        return f"Hello {self.name} your current balance is {self.balance}"
    def withdraw(self,amount):
        if amount<=self.balance and amount>0: 
          transaction=amount+100      
          self.balance-=transaction
          self.withdrawals.append(amount)
          details={"Date":strftime("%d/%m/%y %H:%M:%S")}
          print(details)
          return f"Hello you have withdrawn {amount} and your current balance is {self.balance}"
        else:
            return f"You cant withdraw!! "  
       
    def deposits_statements(self):
        for x in self.deposits:
            print(f"Hello you have deposited {x}" ,end="\n")

    def withdrawals_statement(self):
        for x in self.withdrawals:
            print(f"Hello you have withdrawn {x}" ,end="\n")
    def current_balance(self):
        return f"Hello your current balance is {self.balance} "    

    def full_statement(self):
        for (x ,y )in zip(self.deposits ,self.withdrawals):
            time=strftime('%H:%M:%S')
            print(f"{time} deposit {x}")
            print(f"{time} withdrawal {y}")

    def borrowing(self,loan):
        self.loan=loan
        sum=0
        for x in self.deposits:
            sum+=x
        print(sum)    
        interest=loan*(3/100)
        total_amount=loan+interest
        self.total_amount=total_amount
        if len(self.deposits)>=10 and self.loan>100 and self.loan<=1/3*(sum) and self.my_balance==0 and self.loan_balance==0:
  
            return f"Hello {self.name} you have succesfully been granted {self.loan} with 3% interest and you'll return as {self.total_amount} "
        else:
            return f"Not eligible for a loan" 

    def loan_repayment(self,paid_amount):
        self.loan_balance+=self.total_amount
        if paid_amount>self.loan_balance:
            overpaid_amount=paid_amount-self.loan_balance
            self.deposits.append(overpaid_amount)
        else:    
            self.loan_balance-=paid_amount
            print(f"Hello {self.name} you have succesfully paid {paid_amount}, and your current loan balance is {self.loan_balance} please pay the remaining amount")
           
 
    def transfer(self,amount,account):
        self.amount=amount
        self.account=account  
        if self.amount<self.balance:
            self.balance-=self.amount
            return f"Succesfully sent {self.amount} to {self.account}, your current balance is {self.balance} "



    




         


    

