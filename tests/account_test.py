from .context import bank


def test_open_returns_an_account() -> None:
    account = bank.open_account()

    assert isinstance(account, bank.Account)


def test_opened_accounts_are_remembered() -> None:
    account = bank.open_account()

    assert account in bank.accounts
