class BankAccount:
    def __init__(self, customer_name: str,):
        self.name = customer_name.strip().title()
        self.money = 0
        self.id = 54878



account_1 = BankAccount("fjfjfsj")
account_2 = BankAccount("fjfjfrrnl")

print(account_1.__dict__, id(account_1))
print(account_2.__dict__, id(account_2))