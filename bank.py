balance = 0

while True:

    print("\n1) Deposit  2) Balance  3) Withdraw  0) Quit")

    choice = int(input("Choice: "))

    if choice == 1:
        amount = float(input("Amount: "))

        if amount > 0:
            balance = balance + amount
        else:
            print("Invalid amount")

    elif choice == 2:
        print(f"Balance: {balance:.2f} €")

    elif choice == 3:
        amount = float(input("Withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance or invalid amount")

    elif choice == 0:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")