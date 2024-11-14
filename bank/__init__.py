import dataclasses


__all__: list[str] = []


@dataclasses.dataclass
class Account:
    closed: bool = False
    balance: int = 0

    def close(self) -> None:
        self.closed = True

    def deposit(self, amount: int) -> None:
        self.balance += amount


accounts: list[Account] = []


def open_account() -> Account:
    account = Account()
    accounts.append(account)
    return account
