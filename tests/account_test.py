import pytest

from .context import bank


def test_open_returns_an_account() -> None:
    account = bank.open_account()

    assert isinstance(account, bank.Account)


def test_opened_accounts_are_remembered() -> None:
    account = bank.open_account()

    assert account in bank.accounts


def test_closing_an_account_marks_it_as_closed() -> None:
    account = bank.open_account()
    account.close()

    assert account.closed


def test_accounts_have_numerical_balance() -> None:
    account = bank.Account()

    assert account.balance == 0


def test_accounts_can_receive_deposits() -> None:
    account = bank.Account()

    account.deposit(100)
    account.deposit(100)

    assert account.balance == 200


def test_deposits_must_be_positive() -> None:
    account = bank.Account()

    with pytest.raises(bank.InvalidAmount):
        account.deposit(-100)

    assert account.balance == 0


def test_accounts_can_receive_withdrawals() -> None:
    account = bank.Account()

    account.withdraw(100)
    account.withdraw(100)

    assert account.balance == -200


def test_withdrawals_must_be_positive() -> None:
    account = bank.Account()

    with pytest.raises(bank.InvalidAmount):
        account.withdraw(-100)

    assert account.balance == 0
