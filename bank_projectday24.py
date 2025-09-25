# This is a basic banking system implementation in Python that allows users to create accounts, log in, deposit and withdraw funds, check balances, and view mini statements. The system consists of two classes: Account and BankingSystem.

# -----------BANKING SYSTEM-------------

class Account:
    def __init__(self, username, password, balance=0,):

        self.username = username
        self.password = password
        self.balance = balance
# the Account class is defined with three instance variables - username, password, and balance. The __init__ method initializes these variables with the arguments passed while creating an object of this class. The class also contains four methods - deposit, withdraw, get_balance, and get_mini_statement.

    def deposit(self, amount):

        self.balance += amount
        print(f"\nAmount deposited: {amount}\nTotal Balance: {self.balance}")
# The deposit method takes an argument amount and adds it to the balance variable. It then prints a message showing the deposited amount and the updated balance.

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(
                f"\nAmount withdrawn: {amount}\nRemaing Balance: {self.balance}")
        else:
            print("Insufficient balance")
# The withdraw method takes an argument amount and checks if the balance is greater than or equal to the amount to be withdrawn. If it is, it deducts the withdrawn amount from the balance and prints a message showing the withdrawn amount and the updated balance. If not, it prints a message saying that there is insufficient balance.

    def get_balance(self):
        return self.balance
# The get_balance method simply returns the current balance.

    def get_mini_statement(self):
        print("Mini statement:")
        print(f"Username: {self.username}")
        print(f"Current balance: {self.balance}")
# The get_mini_statement method prints the username and current balance of the account.


class BankingSystem:
    def __init__(self):
        self.accounts = {}
# the BankingSystem class is defined. It has one instance variable - accounts - which is a dictionary that stores the username as key and the Account object as value.

    def create_account(self, username, password):
        if username in self.accounts:
            print("Username already exists")
        else:
            self.accounts[username] = Account(username, password)
            print("\nAccount created successfully")
            print("-------Welcome to PYTHON Bank-------")
# The create_account method takes two arguments - username and password. It checks if the username already exists in the accounts dictionary. If it does, it prints a message saying that the username already exists. If it does not, it creates a new Account object with the given username and password and adds it to the accounts dictionary. It then prints a message saying that the account was created successfully.

    def login(self, username, password):
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login Sucess....")
                return account
            else:
                print("Invalid password")
        else:
            print("Invalid username")
        return None
# The login method takes two arguments - username and password. It checks if the given username exists in the accounts dictionary. If it does, it retrieves the corresponding Account object and checks if the given password matches the password of that account. If it does, it prints a message saying that the login was successful and returns the Account object. If it does not, it prints a message saying that the password is invalid. If the given username is not found in the accounts dictionary, it prints a message saying that the username is invalid.


bank = BankingSystem()

while True:
    print("\n")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
# the main program loop is defined inside the if __name__ == '__main__': block. It creates a new BankingSystem object and presents a menu of options to the user - create an account, login, or exit.
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.create_account(username, password)
# If the user chooses to create an account, the program prompts the user to enter a username and password. It then calls the create_account method of the BankingSystem object with these arguments.

    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        account = bank.login(username, password)
        if account is not None:
            while True:
                print("\n-----Welcome to PYTHON Bank-----")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check balance")
                print("4. Mini statement")
                print("5. Logout\n")
                choice = input("Enter your choice (1-5): ")
# If the user chooses to login, the program prompts the user to enter their username and password. It then calls the login method of the BankingSystem object with these arguments. If the login is successful, it presents the user with a menu of options - deposit, withdraw, check balance, print mini-statement, or logout.

                if choice == '1':
                    amount = int(input("Enter amount to deposit: "))
                    account.deposit(amount)

                elif choice == '2':
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
# If the user chooses to deposit or withdraw, the program prompts the user to enter the amount to deposit or withdraw. It then calls the corresponding method of the Account object.

                elif choice == '3':
                    print(f"Current balance: {account.get_balance()}")
# If the user chooses to check their balance, the program calls the get_balance method of the Account object and prints the current balance.

                elif choice == '4':
                    account.get_mini_statement()
# If the user chooses to print a mini-statement, the program calls the get_mini_statement method of the Account object and prints the username and current balance.

                elif choice == '5':
                    print("\n--------THANK YOU VISIT AGAIN--------")
                    break
# If the user chooses to logout, break out of the inner WHILE loop and display a message saying "THANK YOU VISIT AGAIN".
                else:
                    print("Invalid choice")
    elif choice == '3':
        print("\n------THANK YOU------")
        break
# If the user selects option 3, a message is printed indicating that they have exited the program, and the break statement is used to exit the outer while loop that displays the main menu.

    else:
        print("Invalid choice")



