class BankAccount :
    
    #Constructor
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Usted ha ingresado {amount}, total de cuenta: {self.balance}")
        else:
            print(f"Usted no tiene una cuenta activa")
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Usted ha retirado {amount}, total en la cuenta: {self.balance}")
            else:
                print("Lo que desea retirar pasa el total de su cuenta")
        else:
            print("Usted no tiene una cuenta activa")
    
    def desactive_account(self):
        self.is_active = False
        print("Su cuenta ha sido desactivada")

    
    def active_account(self):
        self.is_active = True
        print("Su cuenta ha sido activada")


account_one = BankAccount("Karen", 500)
account_two = BankAccount("Luis", 2000)

# account_one.withdraw(200)
account_two.desactive_account()
account_two.withdraw(100)
account_two.active_account()
account_two.deposit(80000)