class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0#An initial balance parameter that defaults to zero

    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if self.account_balance >= amount:#Check if balance is sufficient
            self.account_balance -= amount
            return True#Returning true for sufficient balance
        else:
            return False#Returning False for insufficient balance
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")