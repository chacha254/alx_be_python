class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(self.__account_balance)
        else:
            print("Cannot deposit a negative value.")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount is to low to withdraw")
            return False
        elif amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            print(f"Insufficient balance in your account, your balance is:{self.__account_balance}")
            return False 
    def display_balance(self):
        print(f"Current balance${self.__account_balance}")