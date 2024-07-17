class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount=0):
        if (
            type(amount) == int or type(amount) == float and amount > 0
        ):  ## verificacao de tipo para amount ser um numero
            self.balance += amount
        else:
            print("Invalid type")  ## verificacao/teste com print

    def withdraw(self, amount=0):
        if (
            type(amount) == int or type(amount) == float and amount > 0
        ):  ## verificacao de tipo para amount ser um numero
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds")
        else:
            print("Invalid type")  ## verificacao/teste com print

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []

    def add_account(self, account):
        if (
            type(account) == Account
        ):  ## verificacao de tipo para add apenas objetos do tipo Account
            self.accounts.append(account)
        else:
            print("Invalid type")  ## verificacao/teste com print

    def get_total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.get_balance()
        return total_balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        if (
            type(customer) == Customer
        ):  ## verificacao de tipo para add apenas objetos do tipo Costumer
            self.customers.append(customer)

    def get_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def transfer(self, from_account, to_account, amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)


def main():
    # Create a bank
    my_bank = Bank("MyBank")

    # Create customers
    alice = Customer("Alice", 1)
    bob = Customer("Bob", 2)

    # Add customers to the bank
    my_bank.add_customer(alice)
    my_bank.add_customer(bob)

    # Create accounts
    alice_account = Account("A001", 1000)
    bob_account = Account("B001", 500)

    # Add accounts to customers
    alice.add_account(alice_account)
    bob.add_account(bob_account)

    # Perform a transfer
    my_bank.transfer(alice_account, bob_account, 300)

    # Check balances
    print("Alice's balance:", alice_account.get_balance())
    print("Bob's balance:", bob_account.get_balance())


if __name__ == "__main__":
    main()
