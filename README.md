Transaction Event Sourcing Kata
===============================

The code in this repository is my implementation of the "bank account transaction event sourcing" exercise that we worked through at Software Crafters North (Manchester, UK) on 14 November 2024.

The plan was simple. Implement code for a bank account, that supports:

- Opening an account
- Closing an account
- Depositing cash in an account
- Withdrawing cash from an account
- Checking the balance

The above was as far as I got.

> [!NOTE]
> **Note to self:** Next time, don't invest any of your evening in updating your [python-template repository] to work cleanly with the latest versions of the available tooling!

Then, the next task was to investigate [event sourcing] or [CQRS], refactoring the solution to use that approach.

[python-template repository]: https://github.com/gma/python-template
[event sourcing]: https://martinfowler.com/eaaDev/EventSourcing.html
[CQRS]: https://martinfowler.com/bliki/CQRS.html

## Running the tests

To get everything installed, so you can run the tests, follow these steps.

Start by creating a virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Now we can install our development tools:

```sh
pip install --upgrade pip
pip install pip-tools
pip-sync dev-requirements.txt
```

The dev tools included in the template are sufficient to be able to run the linter, type checker, and tests. They're all run by this script:

```sh
./test
```
