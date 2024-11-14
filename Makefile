.PHONY: default
check: lint format types

.PHONY: lint
lint:
	ruff check .

.PHONY: format
format:
	ruff format --check .

.PHONY: types
types:
	mypy .
