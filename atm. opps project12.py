class ATM:
    def __init__(self, bank_name, location):
        self.bank_name = bank_name
        self.location = location
        self.amount = 0  # Initially set amount to 0
        self.amount_debited = 0

    def credit(self, amount):
        self.amount += amount
        print(f"Amount credited is {amount}")

    def debit(self, amount_debited):
        self.amount_debited += amount_debited
        print(f"Amount debited is {amount_debited}")

    def balance(self):
        result = self.amount - self.amount_debited
        print(f"Balance amount is {result}")

# Creating an object and using the methods
obj_BoI = ATM('BOI', 'Hyderabad')
obj_BoI.credit(10000)
obj_BoI.debit(5000)
obj_BoI.balance()
