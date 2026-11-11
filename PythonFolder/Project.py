class BankAccount:
    def __init__(self, Balance, Name, Pin):
        self.Balance = Balance
        self.Name = Name
        self.Pin = Pin

    def CheckPasscode(self, pinamt):
        if pinamt == self.Pin:
            print("Sucessfully signed in to your account.")
        else:
            print("Please try again.")
            
    
    def CheckBalance(self):
        print(f"{self.Name} has ${self.Balance} on their account.")

    def Deposit(self, depoAmt):
        self.Balance = self.Balance + depoAmt
        print(f"{self.Name} now has ${self.Balance} on their account.")

    def Withdraw(self, withdrawAmt):
        if withdrawAmt > self.Balance:
            print("Cannot proceed with this action. Please try again.")
        else:
            self.Balance = self.Balance - withdrawAmt
            print(f"{self.Name} now has ${self.Balance} on their account.")

            

    


        