class BankAccount:
    bank_name = "GPT Bank"
    new_bank = "Dany Bank" 

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    @classmethod
    def change_bank(cls, name: str):
        cls.bank_name = name

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance:.2f}, bank='{self.bank_name}')"


def main():
    acc = BankAccount("Alice", 100.0)
    acc.deposit(50)
    try:
        acc.withdraw(100)
    except ValueError as e:
        print("Blocked:", e)
    print(acc)
    BankAccount.change_bank("Test Bank")
    print("Changed bank:", BankAccount.bank_name)

if __name__ == "__main__":
    main()
