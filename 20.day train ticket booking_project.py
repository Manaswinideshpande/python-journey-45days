import random

class Train:
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats

    def display_info(self):
        print(f"\nTrain Number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Available Seats: {self.seats}")

    def book_tickets(self, num_tickets):
        if num_tickets > self.seats:
            return None
        else:
            pnr_list = []
            for _ in range(num_tickets):
                pnr_list.append(random.randint(100000, 999999))
            self.seats -= num_tickets
            return pnr_list


class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display_info(self):
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone: {self.phone}")


class Ticket:
    def __init__(self, train, source, destination, passengers, pnrs):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnrs = pnrs

    def display_info(self):
        print("\n🎫 Ticket Details:")
        print(f"Train Number: {self.train.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        for i, passenger in enumerate(self.passengers):
            passenger.display_info()
            print(f"PNR: {self.pnrs[i]}")


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password


def main():
    accounts = [
        Account("user1", "password1"),
        Account("user2", "password2")
    ]
    logged_in_account = None

    while True:
        print("\n==== Train Ticket Booking System ====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            accounts.append(Account(username, password))
            print(" Account created successfully!")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")

            for account in accounts:
                if account.username == username and account.check_password(password):
                    logged_in_account = account
                    break

            if logged_in_account:
                print(f"\n Login successful! Welcome, {logged_in_account.username}.")

                # List of available trains
                trains = [
                    Train("12658", "Tirupathi", "Secunderabad", 13),
                    Train("13615", "Tirupathi", "Kachiguda", 12)
                ]

                print("\nAvailable Trains:")
                for train in trains:
                    train.display_info()

                while True:
                    train_num = input("\nEnter Train Number to book: ")
                    selected_train = None
                    for train in trains:
                        if train.train_num == train_num:
                            selected_train = train
                            break

                    if not selected_train:
                        print(" Invalid train number. Try again.")
                        continue

                    try:
                        num_tickets = int(input("Enter number of tickets: "))
                        if num_tickets <= 0:
                            raise ValueError("Number of tickets must be greater than 0.")
                        if num_tickets > selected_train.seats:
                            raise ValueError(f"Only {selected_train.seats} seats are available.")
                    except ValueError as e:
                        print(f" Error: {e}")
                        continue

                    # Collect passenger info
                    passengers = []
                    for i in range(num_tickets):
                        print(f"\nEnter details for passenger {i + 1}:")
                        name = input("Name: ")
                        try:
                            age = int(input("Age: "))
                            if age <= 0 or age > 110:
                                raise ValueError("Invalid age.")
                        except ValueError as e:
                            print(f" Error: {e}")
                            break
                        gender = input("Gender: ")
                        phone = input("Phone: ")
                        passengers.append(Passenger(name, age, gender, phone))

                    # Attempt booking
                    pnrs = selected_train.book_tickets(num_tickets)
                    if pnrs is None:
                        print(" Booking failed. Not enough seats.")
                    else:
                        print("\n Tickets booked successfully!")
                        ticket = Ticket(selected_train, selected_train.source, selected_train.destination, passengers, pnrs)
                        ticket.display_info()
                    break
            else:
                print(" Invalid username or password.")

        elif choice == "3":
            print("👋 Exiting the program. Goodbye!")
            break

        else:
            print(" Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()



            
                 
                    
        
        