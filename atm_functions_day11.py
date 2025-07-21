def atm_choice():
    balance = 5000
    while True:
        choice = input("Enter the number of your choice (1-4):")
        if choice == '1':
            amount = float(input("Enter amount to credit: "))
            balance += amount
        elif choice == '2':
            amount = float(input("Enter amount to debit: "))
            if amount <= balance:
                balance -= amount
            else:
                print("Insufficient balance.")
        elif choice == '3':
            print(f"Your current balance is: ${balance}")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
atm_choice()