# Simple ATM
balance = 5000

while True:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Amount deposited successfully")
            print("Updated balance:", balance)
        else:
            print("Enter a valid amount")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful")
            print("Updated balance:", balance)
        else:
            print("Invalid amount or insufficient balance")

    elif choice == 4:
        print("Thank you! Exiting ATM.")
        break

    else:
        print("Invalid choice. Try again.")
