class BankAccount:
    amount = 0
    #initializes the bank account balance to the value of the input argument
    def __init__(self, amount):
        self.amount = amount

    #takes an amount as input and withdraws it from the balance
    def withdraw(self,amount):
        self.amount=self.amount - amount

    #takes an amount as input and adds it to the balance
    def deposit(self,amount):
        self.amount=self.amount + amount

    #returns the balance on the account    
    def balance(self):
        return self.amount


        
