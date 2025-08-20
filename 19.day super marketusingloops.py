from datetime import datetime

# Input: Customer Name
name = input("Enter your Name: ")

# Dictionary of items and prices
items = {
    "rice": "150/kg",
    "dal": "90/kg",
    "nuts": "250/kg",
    "oil": "150/litre",
    "salt": "20/kg",
    "flour": "50/kg",
    "britania": "50/250grms"
}

# Initialize lists and totals
pricelist = []
ilist = []
qlist = []
plist = []
totalprice = 0

# Main menu loop
while True:
    option = input("\nPress 1 to view item list or 2 to exit: ")

    if option == "2":
        print("Thank you for shopping!")
        break

    elif option == "1":
        print("\nAvailable items:")
        for item, price in items.items():
            print(f"- {item.title()}: {price}")

        # Purchase loop
        while True:
            inp1 = input("\nTo buy press 1 or press 2 to exit: ")

            if inp1 == '2':
                print("Thank you for shopping!")
                break

            elif inp1 == '1':
                item = input("Choose your item: ").strip().lower()

                if item in items:
                    try:
                        unit_price = int(items[item].split('/')[0])
                    except ValueError:
                        print("Invalid price format for item.")
                        continue

                    # Quantity input validation
                    while True:
                        quantity_input = input("Enter quantity (in numbers): ")
                        if quantity_input.isdigit():
                            quantity = int(quantity_input)
                            break
                        else:
                            print("x Please enter a valid number.")

                    # Calculations
                    price = quantity * unit_price
                    pricelist.append((item, quantity, unit_price, price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                    print(f"*{item.title()} added to cart.")
                else:
                    print("x Item not available. Try again.")
            else:
                print("x Invalid input. Please try again.")

        # Show bill if items were purchased
        if totalprice > 0:
            tax = round((totalprice * 12) / 100, 2)
            finalamount = totalprice + tax

            print("\n" + "="*25, "Pythonlife Supermarket", "="*25)
            print(" " * 28 + "Hyderabad")
            print(f"Customer Name: {name}")
            now = datetime.now()
            print("Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
            print("-"*75)
            print("{:<6} {:<15} {:<10} {:<10}".format("SNo", "Item", "Qty", "Price"))
            for i in range(len(pricelist)):
                print("{:<6} {:<15} {:<10} {:<10}".format(i+1, ilist[i], qlist[i], plist[i]))
            print("-"*75)
            print(f"{' ' * 50}Total: Rs {totalprice}")
            print(f"{' ' * 50}Tax (12%): Rs {tax}")
            print(f"{' ' * 50}Final Amount: Rs {finalamount}")
            print("="*75)
            print(" " * 20 + "Thank you & Visit Again!")
            print("="*75 + "\n")

        break  # Exit main menu after billing

    else:
        print("x Invalid option. Please try again.")

