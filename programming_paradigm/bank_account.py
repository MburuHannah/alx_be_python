class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance=account_balance
    def deposit(self, amount):
        if amount >0:
            self.account_balance += amount
            return self.account_balance
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self,amount):

            if amount>self.account_balance:
                print("Sorry, you have insufficient balance in your account")
                return False
            else:
             self.account_balance-=amount
            print(f"Withdrawal successful")
            return True
        
    def display_balance(self):        
        print(f"Current Balance:  {self.account_balance}")
        
        
    
        
        
      