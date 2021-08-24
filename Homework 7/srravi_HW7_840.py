class BankAccount:
    #initializes the bank account balance to the value of the input argument
    def __init__(self, balance=0):
        #if it's less than 0 print corresponding message
        if balance < 0:
            raise ValueError("Illegal balance")
        self.balance = balance
        
    #return the balance on the account
    def balance(self):
        return self.balance
    
    #takes an amount as input and withdraws it from the balance
    def withdraw(self, x):
        #check if it is less than the balance amount
        if x <= self.balance:
            self.balance -= x
        else:
            raise ValueError("Overdraft")
        
    #adds the input value to the amount balance
    def deposit(self, x):
        #check if value is less than 0
        if x < 0:
            raise ValueError("Negative deposit")
        self.balance += x
  
x = BankAccount(-5)
