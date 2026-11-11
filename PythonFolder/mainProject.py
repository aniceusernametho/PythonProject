from Project import BankAccount

Bank1 = BankAccount(5000, "Madav", "2345")


print("Welcome to our Netbanking! How may I help you?")
print("----------------------------------------------")
print("1:Check account balance")
print("2:Deposit amount to an account")
print("3:Withdraw amount from an account")
print("4:Exit")

while True:
    option = str(input("Choose an option.(1/2/3/4)"))
    if option == "1":
        Bank1.CheckBalance()
    elif option == "2":
        Depo = int(input("Enter the amount to deposit."))
        Bank1.Deposit(Depo)
    elif option == "3":
        Withdraw = int(input("Enter the amount to withdraw."))
        Bank1.Withdraw(Withdraw)
    else:
        print("Thank you for using our services.")
        break
        
    
    