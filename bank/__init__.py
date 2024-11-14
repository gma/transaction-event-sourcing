import dataclasses


__all__: list[str] = []


@dataclasses.dataclass
class Account:
    closed: bool = False
    balance: int = 0

    def close(self) -> None:
        self.closed = True

    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise InvalidAmount(f'Deposits must be positive: {amount}')
        self.balance += amount


class InvalidAmount(RuntimeError):
    pass


accounts: list[Account] = []


def open_account() -> Account:
    account = Account()
    accounts.append(account)
    return account
