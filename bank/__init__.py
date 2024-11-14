__all__: list[str] = []


class Account: ...


accounts: list[Account] = []


def open_account() -> Account:
    account = Account()
    accounts.append(account)
    return account
